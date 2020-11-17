from django.contrib import admin

# Register your models here.
from dashboard.models import Post, Profile, Mail

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Mail)