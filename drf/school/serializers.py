from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import School
from university.models import University


class SchoolSerializer(CountryFieldMixin, serializers.ModelSerializer):
    universities = serializers.HyperlinkedRelatedField(
        many=True, queryset=University.objects.all(), view_name='university-detail')

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
