from django.contrib import admin
from models import *

class TrendAdmin(admin.ModelAdmin):
    list_display = ("id", "topic", "author", "time")
    search_fields = ("topic",)
    list_filter = ("time",)


admin.site.register(Trend, TrendAdmin)
