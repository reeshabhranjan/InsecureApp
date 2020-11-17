from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    body = models.TextField(null=False, blank=False)
    time_added = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
