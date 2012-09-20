from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication, Authentication
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from django.db import models
from tastypie.models import create_api_key

from notification.models import ShoutNotification
from shout.api import ShoutResource
from account.api import AccountResource


class ShoutNotificationResource(ModelResource):
    shout = fields.ForeignKey(ShoutResource, "shout")
    receiver = fields.ForeignKey(AccountResource, "receiver")
    class Meta:
        queryset = ShoutNotification.objects.all()
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get', 'put']

    filtering = {
        "shout" : ALL_WITH_RELATIONS,
        "receiver" : ALL_WITH_RELATIONS,
        "status" : ALL,
    }

