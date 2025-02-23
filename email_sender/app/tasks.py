from time import sleep

from celery import shared_task
from django.core.mail import send_mail

from email_sender import settings


@shared_task()
def send_email_task(subject, message, email):
    sleep(5)
    send_mail(subject, message,
              settings.EMAIL_HOST_USER,
              [email], fail_silently=False)
