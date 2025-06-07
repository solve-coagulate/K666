from django import template
from ..models import Comment

register = template.Library()

@register.simple_tag
def user_vote(comment: Comment, user):
    return comment.user_vote(user)
