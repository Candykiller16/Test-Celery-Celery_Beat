from django.core.mail import send_mail

from core import settings


def send(user_email):
    send_mail(
        'Поздравляем! Вы подписались на рассылку',
        'Мы оповестим вас о новшествах нашего сервиса, спасибо за внимание',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )