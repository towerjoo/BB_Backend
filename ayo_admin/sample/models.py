from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sample(models.Model):
    user = models.ForeignKey(User, related_name="sample_user")
    name = models.CharField(max_length=20)
    time = models.DateTimeField()

