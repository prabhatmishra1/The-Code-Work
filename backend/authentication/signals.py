from . models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail


@receiver(post_save, sender=User)
def post_save_generator_code(sender, instance, created, *agrgs, **kwargs):
    if created:
        Code.objects.create(user=instance)


@receiver(post_save, sender=User)
def post_save_send_welcome_email(sender, instance, created, *agrgs, **kwargs):
    if created:
        subject = 'Thank you for registering to our site'
        message = ' Welcome in the world '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        try:
            send_mail(subject, message, email_from, recipient_list)
        except:
            pass
