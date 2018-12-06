from localflavor.us.models import USStateField
from django_countries.fields import CountryField
from django.db import models


class CommonModel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    state = USStateField(null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
