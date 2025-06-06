from django.urls import include, path
from django.contrib import admin
import freek666.views as freek_views
from . import urls as comment_urls

urlpatterns = [
    path('messages/', freek_views.message_inbox, name='messages_inbox'),
    path('messages/compose', freek_views.message_compose, name='messages_compose'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += comment_urls.urlpatterns
