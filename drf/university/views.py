from .serializers import UniversitySerializer
from .models import University
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)


class UniversityListCreate(ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
