from rest_framework import viewsets

from course.models import Course
from course.serliazers import CourseSerializer

from users.permissions import IsModerator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    # permission_classes = [IsModerator]

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)
