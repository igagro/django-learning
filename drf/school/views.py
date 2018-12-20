from .serializers import SchoolSerializer
from .models import School
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework import permissions
from pkg.permissions import CanAddObject, CanEditOrRemoveObject


class SchoolListCreate(ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, CanAddObject]
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, CanEditOrRemoveObject]
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
