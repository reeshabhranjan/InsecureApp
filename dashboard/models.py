from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from dashboard.methods import generate_token


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    time_added = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    secret = models.CharField(max_length=32, default=generate_token)


class Mail(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='sender', null=True)
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='receiver', null=True)
    message = models.TextField(null=False, blank=False)
