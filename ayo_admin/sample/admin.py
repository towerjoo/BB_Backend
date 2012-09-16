from django.contrib import admin

from models import Sample

class SampleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sample, SampleAdmin)

