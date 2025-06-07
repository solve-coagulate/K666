from django.urls import path
from django.views.generic.base import TemplateView

from .views import UserListView

urlpatterns = [
    path('index.html', TemplateView.as_view(template_name="index.html")),
    path('users/', UserListView.as_view(), name='user_list'),
]
