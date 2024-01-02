from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from celery_test import settings


@shared_task(bind=True)
def send_email(self):
    users = get_user_model().objects.all()
    for user in users:
        subject = "Hello Celery"
        message = "This is a test email."
        to_email = [user.email]
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=to_email,
            fail_silently=True,
        )
    return "Task done successfully!"
