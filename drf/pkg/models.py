from django.db import models


class CommonDates(models.Model):
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
