from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.models import Course
from lesson.models import Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = '__all__'
