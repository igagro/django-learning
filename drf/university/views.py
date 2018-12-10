from .serializers import UniversitySerializer
from school.serializers import SchoolSerializer
from .models import University
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     ListAPIView)


class UniversityListCreate(ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityDetail(RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversitySchoolsList(ListCreateAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        university = University.objects.get(
            pk=self.kwargs.get('pk'))
        return university.schools.all()


class UniversitySchoolDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        university = University.objects.get(
            pk=self.kwargs.get('pk'))
        school = university.schools.filter(pk=self.kwargs.get('pk_school'))
        return school
