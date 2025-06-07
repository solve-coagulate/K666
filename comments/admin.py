from django.contrib import admin
from .models import Comment, ModerationVote

admin.site.register(Comment)


class ModerationVoteAdmin(admin.ModelAdmin):
    list_display = ("comment", "user", "value", "created_on")
    list_filter = ("value", "created_on")
    search_fields = ("comment__text", "user__username")


admin.site.register(ModerationVote, ModerationVoteAdmin)

# Register your models here.
