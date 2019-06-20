from rest_framework import serializers
from exampleapi.models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'category', 'max_participants')
