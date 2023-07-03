import json
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django_eventstream import send_event


class BroadcastNotification(models.Model):
    message = models.TextField()


@receiver(post_save, sender=BroadcastNotification)
def notification_handler(sender, instance, created, **kwargs):
    chanel_layer = get_channel_layer()
    # send_event(
    #     'notification_broadcast',
    #     'send_notification',
    #     data=instance.message,
    # )
    async_to_sync(chanel_layer.group_send)(
        "notification_broadcast", {
            'type': 'send_notification',
            'message': json.dumps(instance.message),
        })
