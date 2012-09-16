from tastypie.resources import ModelResource
from models import Sample
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication

from django.db import models
from tastypie.models import create_api_key

models.signals.post_save.connect(create_api_key, sender=User)

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        excludes = ["email", "password"]
        authorization = Authorization()
        authentication = ApiKeyAuthentication()

class SampleResource(ModelResource):
    user = fields.ForeignKey(UserResource, "user")
    class Meta:
        queryset = Sample.objects.all()
        authorization = Authorization()
        authorization = ApiKeyAuthentication()

