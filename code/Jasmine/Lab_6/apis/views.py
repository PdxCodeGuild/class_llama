from rest_framework import viewsets

from students import models
from .serializers import StudentSerializer
from .permissions import IsAuthororReadOnly

# class ListStudent(generics.ListCreateAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = StudentSerializer


# class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = StudentSerializer

class StudentViewSet(viewsets.ModelViewSet): 
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthororReadOnly]
