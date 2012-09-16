from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="venues/%Y/%m/%d", null=True, blank=True) 
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_edit_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name


