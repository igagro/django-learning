from .serializers import UniversitySerializer, UniversitySchoolSerializer
from school.serializers import SchoolSerializer
from .models import University, UniversitySchools
from pkg.permissions import CanAddObject, CanEditOrRemoveObject
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework import permissions


class UniversityListCreate(ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, CanAddObject]
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, CanEditOrRemoveObject]
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversitySchoolsList(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CanAddObject]
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
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, CanEditOrRemoveObject]
    serializer_class = UniversitySchoolSerializer
    lookup_field = 'school_id'

    def get_queryset(self):
        return UniversitySchools.objects.filter(
            university=self.kwargs.get('university_id'))
