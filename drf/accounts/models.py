from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_profile_image(instance, filename):
    return "accounts/{user}/{filename}".format(user=instance.user,
                                               filename=filename)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    image_url = models.ImageField(
        upload_to=upload_profile_image, null=True, blank=True)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
