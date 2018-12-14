from .serializers import UniversitySerializer, UniversitySchoolSerializer
from school.serializers import SchoolSerializer
from .models import University, UniversitySchools
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)


class UniversityListCreate(ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityDetail(RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversitySchoolsList(ListCreateAPIView):
    serializer_class = UniversitySchoolSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'university_id': self.kwargs.get('university_id')
        })
        return context

    def get_queryset(self):
        return UniversitySchools.objects.filter(
            university=self.kwargs.get('university_id'))


class UniversitySchoolDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = UniversitySchoolSerializer
    lookup_field = 'school_id'

    def get_queryset(self):
        return UniversitySchools.objects.filter(
            university=self.kwargs.get('university_id'))
