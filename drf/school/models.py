from django.db import models
from pkg.models import AbstractModel


def upload_logo_image(instance, filename):
    return "school/{school}/{filename}".format(school=instance.name,
                                               filename=filename)


class School(AbstractModel):
    logo_url = models.ImageField(
        upload_to=upload_logo_image,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
