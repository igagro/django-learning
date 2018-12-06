from rest_framework import serializers
from .models import University


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name', 'address', 'city', 'country', 'state',
                  'description', 'logo_url', 'created_at', 'modified_at')
