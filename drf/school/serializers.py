from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import School
from university.models import University


class SchoolSerializer(CountryFieldMixin, serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ('name',
                  'address',
                  'city',
                  'country',
                  'state',
                  'description',
                  'logo_url',
                  'created_at',
                  'modified_at',
                  'universities'
                  )
