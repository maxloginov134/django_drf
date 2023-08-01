from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from users.models import User


@shared_task
def check_last_login():
    users = User.objects.all()
    for user in users:
        if user.last_login:
            if (timezone.now() - user.last_login).days > 30:
                user.is_active = False
                send_mail(
                    subject='Блокировка',
                    message='Вы заблокированны так как не пользуетесь нашим ресурсом',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=user.email,
                    fail_silently=False,
                    auth_user=settings.EMAIL_HOST_USER,
                    auth_password=settings.EMAIL_HOST_PASSWORD,
                )
                user.save()
