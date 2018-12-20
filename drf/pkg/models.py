from django.db import models
from localflavor.us.models import USStateField
from django_countries.fields import CountryField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CommonModel(BaseModel):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    state = USStateField(null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        abstract = True


class Role(models.Model):
    ROLE_CHOICES = (
        ('UNV', 'University'),
        ('SCH', 'School')
    )
    role_type = models.CharField(
        max_length=3, choices=ROLE_CHOICES, null=True, blank=True
    )
    name = models.CharField(
        max_length=30, null=True, blank=True
    )
    permissions = models.ManyToManyField(
        'Permission',
        through='RolePermission',
        related_name='roles')

    def __str__(self):
        return self.name


class Permission(models.Model):
    PERMISSIONS_CHOICES = (
        ('ADD', 'AddPermission'),
        ('EDIT', 'EditPermission'),
        ('DELETE', 'DeletePermission'),
    )
    name = models.CharField(
        max_length=6, choices=PERMISSIONS_CHOICES, null=True, blank=True
    )

    def __str__(self):
        return self.name


class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
