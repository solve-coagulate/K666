from django.urls import include, path

from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('index.html', TemplateView.as_view(template_name="index.html")),
    # path(r'^$', RedirectView.as_view(url="/index.html")),
]
