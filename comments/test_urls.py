from django.urls import path
from django.urls import include
import freek666.views as freek_views
from . import urls as comment_urls

urlpatterns = [
    path('messages/', freek_views.message_inbox, name='messages_inbox'),
    path('messages/compose', freek_views.message_compose, name='messages_compose'),
    path('accounts/', include('allauth.urls')),
]
urlpatterns += comment_urls.urlpatterns
