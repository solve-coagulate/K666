from django import forms
from .models import Comment

class CommentForm(forms.Form):
    comment_text = forms.CharField(required=True)
    parent_comment_id = forms.IntegerField(required=False)

    def clean_parent_comment_id(self):
        parent_id = self.cleaned_data.get('parent_comment_id')
        if parent_id is None:
            return None
        try:
            return Comment.objects.get(id=parent_id)
        except Comment.DoesNotExist:
            raise forms.ValidationError("Invalid parent comment")


class CommentFormOptionalText(CommentForm):
    """Variant of :class:`CommentForm` where ``comment_text`` is optional."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["comment_text"].required = False

