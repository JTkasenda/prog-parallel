# myapp/tasks.py
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    send_mail(
        'Welcome to My App',
        'Thank you for signing up!',
        'jeantshimbalanga9@gmail.com.com',
        [user_email],
        fail_silently=False,
    )