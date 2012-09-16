from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication, Authentication

from django.db import models
from tastypie.models import create_api_key

from account.models import Account, FollowRelation, ContactGroup


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        excludes = ["email", "password"]
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        #authentication = Authentication()

class AccountResource(ModelResource):
    user = fields.ForeignKey(UserResource, "user")
    class Meta:
        queryset = Account.objects.all()
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        #authentication = Authentication()
