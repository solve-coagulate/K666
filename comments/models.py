from django.db import models
from django.contrib.auth.models import User
import re

SUBJECT_LENGTH=120

def find_fold(text):
    splits = re.findall('^---+$', text, flags=re.MULTILINE)
    if not splits:
        return None
    return re.search('^-{%d}$' % max([len(s) for s in splits]), text, flags=re.MULTILINE)

class Comment(models.Model):
    text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'Comment', null=True, blank=True, db_index=True, on_delete=models.CASCADE
    )
    
    class Meta:
        ordering = ['-id']
    
    # edited_by = models.ForeignKey(User)
    # edited_on = models.DateTimeField(auto_now=True)

    def subject(self):
        "Gets the subject from the comment text"
        cleaned = self.text.replace('\r\n', '\n')
        lines = cleaned.split('\n')
        first_line = lines[0]
        if len(first_line)>SUBJECT_LENGTH:
            return first_line[:SUBJECT_LENGTH] + "..."
        else:
            return first_line
    
    def body(self):
        "Gets the body from the comment text"
        cleaned = self.text.replace('\r\n', '\n')
        lines = cleaned.split('\n')
        first_line = lines[0][SUBJECT_LENGTH:]
        lines[0]=first_line
        
        if lines[0] == "":
            lines = lines[1:]
        
        if len(lines) and lines[0] == "":
            lines = lines[1:]

        return '\n'.join(lines)

    def story_intro(self):
        body = self.body()
        fold = find_fold(body)
        if fold:            
            lines = body[:fold.span()[0]].split('\n')
            if len(lines) and lines[-1] == "":
                lines = lines[:-1]
            return '\n'.join(lines)
        return body
        
    def story_body(self):
        body = self.body()
        fold = find_fold(body)
        if fold:
            lines = body[fold.span()[1]:].split('\n')
            if len(lines) and lines[0] == "":
                lines = lines[1:]
            if len(lines) and lines[0] == "":
                lines = lines[1:]
            return '\n'.join(lines)
        return ""
    
    def replies(self):
        """Return the total number of descendant comments."""

        total = 0
        queue = [self.id]

        while queue:
            children = list(
                Comment.objects.filter(parent_id__in=queue).values_list("id", flat=True)
            )
            total += len(children)
            queue = children

        return total

    def __str__(self):
        return "Comment: #%d by %s on %s --- %s" % (self.id or 0, self.created_by, self.created_on, self.text[:120])
