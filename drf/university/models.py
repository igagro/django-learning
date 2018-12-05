from django.db import models
from pkg.models import CommonDates


def upload_logo_image(instance, filename):
    return "university/{user}/{filename}".format(user=instance.user,
                                                 filename=filename)


class University(CommonDates):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    logo_url = models.ImageField(
        upload_to=upload_logo_image, null=True, blank=True)
