"""k666 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  re_path(r'^blog/', include(blog_urls))
"""
from django.urls import include, path, re_path
from django.contrib import admin

import comments

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('freek666.urls')),
    path('accounts/', include('allauth.urls')),
    # Temporary disable django_messages until a compatible release is available
    # path('messages/', include('django_messages.urls')),
    path('comments/', include('comments.urls')),
    path('', comments.views.story_list ),
    
]
