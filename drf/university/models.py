from django.db import models
from pkg.models import CommonModel
from school.models import School


def upload_logo_image(instance, filename):
    return "university/{unv}/{filename}".format(unv=instance.name,
                                                filename=filename)


class University(CommonModel):
    schools = models.ManyToManyField(School, through='UniversitySchools',
                                     related_name='universities')
    logo_url = models.ImageField(
        upload_to=upload_logo_image,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class UniversitySchools(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    is_main_school = models.BooleanField(default=False)
