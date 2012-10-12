from django.contrib import admin
from models import *

class ShoutAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "group", "venue", "type", "is_featured")
    search_fields = ("content",)
    list_filter = ("type", "is_featured", "time", )

class ShoutCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "shout", "commenter")
    search_fields = ("content",)
    list_filter = ("comment_time",)

class ShoutReportAdmin(admin.ModelAdmin):
    list_display = ("id", "shout", "reporter")
    search_fields = ("content",)
    list_filter = ("report_time",)


admin.site.register(Shout, ShoutAdmin)
admin.site.register(ShoutComment, ShoutCommentAdmin)
admin.site.register(ShoutReport, ShoutReportAdmin)
