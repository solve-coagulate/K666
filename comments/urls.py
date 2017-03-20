from django.conf.urls import include, url

from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView

from .views import list, story_list, story_detail, add, detail, reply, ajax_preview, ajax_add, ajax_comment_form

urlpatterns = [
    url(r'^list.html$', list, name="comment-list"),
    url(r'^story_list.html$', story_list, name="story-list"),
    url(r'^story/(?P<id>[0-9]+)$', story_detail, name="story-detail"),
    url(r'^add.html$', add, name="add-comment"),
    url(r'^comment/(?P<id>[0-9]+)$', detail, name="comment-detail"),
    url(r'^reply/(?P<id>[0-9]+)$', reply, name="comment-reply"),
    url(r'^ajax_preview.html$', ajax_preview, name="ajax-preview-comment"),
    url(r'^ajax_add.html$', ajax_add, name="ajax-add-comment"),
    url(r'^ajax_comment_form.html$', ajax_comment_form, name="ajax-comment-form"),
]