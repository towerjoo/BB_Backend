from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication, Authentication
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from django.db import models
from tastypie.models import create_api_key

from venue.models import Venue


class VenueResource(ModelResource):
    class Meta:
        queryset = Venue.objects.all()
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get', 'put']

        filtering = {
            "name" : ALL,
            "longitude" : ALL,
            "latitude" : ALL,
        }

