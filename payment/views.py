import stripe as stripe
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from config import settings
from payment.models import Payment
from payment.serializers import PaymentSerializers
from payment.services import create_payment, checkout_session


class PaymentBaseAPIView:
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()


class PaymentListAPIView(PaymentBaseAPIView, generics.ListAPIView):
    """Вью возвращающая список платежей"""

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ("course", "kind_of_payment")
    ordering_fields = ("date_pay",)


class PaymentCreateAPIView(generics.CreateAPIView):
    """Вью создающая платеж"""

    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        session = checkout_session(
            course=serializer.validated_data['course'],
            user=self.request.user
        )
        serializer.save()
        create_payment(course=serializer.validated_data['course'],
                       user=self.request.user,
                       session=session)

        return Response(session['id'], status=status.HTTP_201_CREATED)


