from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_eventstream import send_event


class Notification(models.Model):
    message = models.TextField()

    def __str__(self) -> str:
        return f'{self.message}'


@receiver(post_save, sender=Notification)
def notification_handler(sender, instance, created, **kwargs):
    send_event(
        'notification_broadcast',
        'message',
        data=instance.message,
    )
