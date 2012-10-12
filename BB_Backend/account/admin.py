from django.contrib import admin
from models import *

class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "gender", "type", "longitude", "latitude", "is_facebook_account")
    search_fields = ("id", "user__username")
    list_filter = ("type", "is_facebook_account", "register_time", "last_login_time", "gender")

class FollowRelationAdmin(admin.ModelAdmin):
    list_display = ("id", "follower", "followee")
    search_fields = ("follower__user__username", "followee__user__username")
    list_filter = ("follow_time", )

class ContactGroupAdmin(admin.ModelAdmin):
    list_display = ("id","name", "owner", )
    list_filter=("create_time",)
    search_fields = ("name", "owner__user__username")
    

admin.site.register(Account, AccountAdmin)
admin.site.register(FollowRelation, FollowRelationAdmin)
admin.site.register(ContactGroup, ContactGroupAdmin)
