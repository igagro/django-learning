from django.contrib.auth import get_user_model
from django.db import models
from pkg.models import Role

from .utils import upload_profile_image


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    image_url = models.ImageField(
        upload_to=upload_profile_image, null=True, blank=True)
    roles = models.ManyToManyField(Role, related_name='profiles')
