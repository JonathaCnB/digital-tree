from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import Profile, User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()

    if not hasattr(instance, "user_profiles"):
        Profile.objects.create(user=instance)
