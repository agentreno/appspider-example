from rest_framework import generics

from exampleapi.models import Course
from exampleapi.serializers import CourseSerializer


# Create your views here.
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
