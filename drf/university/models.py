from django.db import models
from pkg.models import CommonModel
from school.models import School


def upload_logo_image(instance, filename):
    return "university/{unv}/{filename}".format(unv=instance.name,
                                                filename=filename)


class University(CommonModel):
    schools = models.ManyToManyField(School)
    logo_url = models.ImageField(
        upload_to=upload_logo_image,
        null=True,
        blank=True
    )

    def __unicode__(self):
        return '%d: %s' % (self.pk, self.name)

    def __str__(self):
        return self.name
