from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from users.models import User
from users.serializers import UserSerializers, UserDetailSerializer
from users.tasks import check_last_login


class UsersListAPIView(ListAPIView):
    serializer_class = UserSerializers

    def get_queryset(self):
        check_last_login()
        return User.objects.all()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserDeleteAPIView(DestroyAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserDetailAPIView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
