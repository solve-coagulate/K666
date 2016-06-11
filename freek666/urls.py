from django.conf.urls import include, url

from django.views.generic.base import RedirectView
# from django.views.generic.base import TemplateView

from .views import *

urlpatterns = [
    # url(r'^index.html$', TemplateView.as_view(template_name="index.html")),
    url(r'^index.html$', RedirectView.as_view(url="/")),
    url(r'^$', IndexView.as_view(template_name="index.html")),
    url(r'^u/$', UserListView.as_view()),
    # url(r'^$', RedirectView.as_view(url="/index.html")),
]
