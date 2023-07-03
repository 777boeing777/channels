from django.contrib import admin
from .models import BroadcastNotification


class NotificationAdmin(admin.ModelAdmin):
    pass


admin.site.register(BroadcastNotification, NotificationAdmin)
