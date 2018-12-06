from localflavor.us.models import USStateField
from django_countries.fields import CountryField
from django.db import models
from pkg.models import CommonDates


def upload_logo_image(instance, filename):
    return "university/{unv}/{filename}".format(unv=instance.name,
                                                filename=filename)


class University(CommonDates):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    state = USStateField(null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    logo_url = models.ImageField(
        upload_to=upload_logo_image, null=True, blank=True)
