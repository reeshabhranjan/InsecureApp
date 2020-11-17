from django.contrib import admin

# Register your models here.
from dashboard.models import Post, Profile

admin.site.register(Post)
admin.site.register(Profile)
