from django.db import models
from django.contrib.auth.models import User

SUBJECT_LENGTH=120

class Comment(models.Model):
    text = models.TextField()
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('Comment', null=True, db_index=True)
    
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

    def __str__(self):
        return "Comment: #%d by %s on %s --- %s" % (self.id or 0, self.created_by, self.created_on, self.text[:120])
