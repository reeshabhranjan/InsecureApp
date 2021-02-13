from django.urls import path
from django.contrib.auth import views as auth_views

from dashboard import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('mails/', views.mail, name='mails'),
    path('send_mail/', views.send_mail, name='send_mail'),
    path('update_username_get/', views.update_username_get, name='update-username-get'),
    path('update_username_post/', views.update_username_post, name='update-username-post'),
]