from django.contrib import admin
from models import *

class ShoutNotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "shout", "receiver", "status")
    search_fields = ("shout__content", "receiver__user__name")
    list_filter = ("status",)


admin.site.register(ShoutNotification, ShoutNotificationAdmin)
