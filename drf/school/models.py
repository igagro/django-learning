from django.db import models
from pkg.models import CommonModel


def upload_logo_image(instance, filename):
    return "school/{school}/{filename}".format(school=instance.name,
                                               filename=filename)


class School(CommonModel):
    logo_url = models.ImageField(
        upload_to=upload_logo_image,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
