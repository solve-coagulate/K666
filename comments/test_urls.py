from django.urls import include, path
from django.contrib import admin
from . import urls as comment_urls

urlpatterns = [
    path('messages/', include('django_messages.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('freek666.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += comment_urls.urlpatterns
