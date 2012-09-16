from django.contrib import admin
from models import *

class VenueAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "longitude", "latitude")
    search_fields = ("name", )
    list_filter = ("create_time", "last_edit_time")


admin.site.register(Venue, VenueAdmin)
