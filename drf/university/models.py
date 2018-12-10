from django.db import models
from pkg.models import AbstractModel
from school.models import School


def upload_logo_image(instance, filename):
    return "university/{unv}/{filename}".format(unv=instance.name,
                                                filename=filename)


class University(AbstractModel):
    schools = models.ManyToManyField(School, related_name='universities')
    main_school = models.ForeignKey(School, on_delete=models.CASCADE)
    logo_url = models.ImageField(
        upload_to=upload_logo_image,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
