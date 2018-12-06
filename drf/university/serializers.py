from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import University
from school.models import School


class UniversitySerializer(CountryFieldMixin, serializers.ModelSerializer):

    class Meta:
        model = University
        fields = ('name',
                  'address',
                  'city',
                  'country',
                  'state',
                  'description',
                  'logo_url',
                  'created_at',
                  'modified_at',
                  'schools'
                  )
