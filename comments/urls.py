from django.urls import include, path, re_path

from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView

from .views import comment_list, story_list, story_detail, add, detail, reply, source, ajax_preview, ajax_add, ajax_comment_form

urlpatterns = [
    re_path(r'^list.html$', comment_list, name="comment-list"),
    re_path(r'^story_list.html$', story_list, name="story-list"),
    re_path(r'^story/(?P<id>[0-9]+)$', story_detail, name="story-detail"),
    re_path(r'^add.html$', add, name="add-comment"),
    re_path(r'^comment/(?P<id>[0-9]+)$', detail, name="comment-detail"),
    re_path(r'^reply/(?P<id>[0-9]+)$', reply, name="comment-reply"),
    re_path(r'^source/(?P<id>[0-9]+)$', source, name="comment-source"),
    re_path(r'^ajax_preview.html$', ajax_preview, name="ajax-preview-comment"),
    re_path(r'^ajax_add.html$', ajax_add, name="ajax-add-comment"),
    re_path(r'^ajax_comment_form.html$', ajax_comment_form, name="ajax-comment-form"),
]
