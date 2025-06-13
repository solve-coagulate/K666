from django.urls import include, path

from . import views

from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('index.html', TemplateView.as_view(template_name="index.html")),
    path('accounts/profile/', views.profile, name='account_profile'),
    # path(r'^$', RedirectView.as_view(url="/index.html")),
]
