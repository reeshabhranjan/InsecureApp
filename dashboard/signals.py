from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from dashboard.models import Profile


@receiver(post_save, sender=User)
def generate_profile(sender, instance, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)