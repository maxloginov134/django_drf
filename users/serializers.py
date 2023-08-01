from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from payment.models import Payment
from users.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):

    payments = SerializerMethodField()

    def get_payments(self, user):
        return [(el.date_pay, el.amount) for el in Payment.objects.filter(user=user)]

    class Meta:
        model = User
        fields = ("email", "phone", "city", "payments")