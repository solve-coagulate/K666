from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from django.contrib.auth.models import User

class IndexView(TemplateView):
    pass

class UserListView(ListView):
    model = User
    template_name = "freek666/userlist.html"
