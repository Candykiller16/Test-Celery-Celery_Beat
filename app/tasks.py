from celery import shared_task
from django.core.mail import send_mail

from app.models import Contact
from app.services import send
from core import settings
from core.celery import app


@shared_task
def add(x, y):
    return x + y


# @shared_task
# def send_beat_email():
#     send_mail(
#         'Вы подписались на рассылку',
#         'Каждые 10 минут мы будем доставать вас',
#         settings.EMAIL_HOST_USER,
#         ['candykiller16@mail.ru'],
#         fail_silently=False,
#     )


@app.task
def send_spam(email):
    send(email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку',
            'Каждые 5 минут мы будем доставать вас',
            settings.EMAIL_HOST_USER,
            [contact.email],
            fail_silently=False,
        )


@shared_task
def send_notifictions():
    print("Hi, I'm here")
