from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import University, UniversitySchools
from django.db import transaction
from school.models import School
from school.serializers import SchoolSerializer


class UniversitySchoolSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()

    class Meta:
        model = UniversitySchools
        fields = ('school', 'is_main_school')

    @transaction.atomic
    def create(self, validated_data):
        university_id = self.context.get('university_id')
        main_school = validated_data.pop('is_main_school')
        if main_school:
            UniversitySchools.objects.filter(
                university=university_id,
                is_main_school=True).update(is_main_school=False)
        school = School.objects.create(**validated_data['school'])
        unv_sch = UniversitySchools.objects.create(university_id=university_id,
                                                   school=school,
                                                   is_main_school=main_school)
        return unv_sch

    @transaction.atomic
    def update(self, instance, validated_data):
        School.objects.filter(pk=instance.school.pk).update(
            **validated_data['school'])
        instance.is_main_school = validated_data.get(
            'is_main_school', instance.is_main_school)
        instance.save()
        return instance


class UniversitySerializer(CountryFieldMixin, serializers.ModelSerializer):
    schools = UniversitySchoolSerializer(
        source="universityschools_set", many=True, read_only=True)

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
