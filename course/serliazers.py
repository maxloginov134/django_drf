from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.models import Course
from lesson.models import Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        return [el.name for el in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = '__all__'
