from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication, Authentication

from django.db import models
from tastypie.models import create_api_key
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from shout.models import Shout, ShoutReport, ShoutComment
from account.api import AccountResource, ContactGroupResource
from venue.api import VenueResource


class ShoutResource(ModelResource):
    author = fields.ForeignKey(AccountResource, "author")
    venue = fields.ForeignKey(VenueResource, "venue")
    group = fields.ForeignKey(VenueResource, "group")
    class Meta:
        queryset = Shout.objects.all()
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        filtering = {
            "author" : ALL_WITH_RELATIONS,
            "venue" : ALL_WITH_RELATIONS,
            "group" : ALL_WITH_RELATIONS,
            "is_featured" : ALL,
            "type" : ALL,

        }

class ShoutCommentResource(ModelResource):
    shout = fields.ForeignKey(ShoutResource, "shout")
    commenter = fields.ForeignKey(AccountResource, "commenter")
    class Meta:
        queryset = ShoutComment.objects.all()
        authorization = Authorization()
        authentication = ApiKeyAuthentication()

        list_allowed_methods = ['get']
        detail_allowed_methods = ['get', 'put']

        filtering = {
            "commenter" : ALL_WITH_RELATIONS,
            "shout" : ALL_WITH_RELATIONS,
        }


class ShoutReportResource(ModelResource):
    shout = fields.ForeignKey(ShoutResource, "shout")
    reporter = fields.ForeignKey(AccountResource, "reporter")
    class Meta:
        queryset = ShoutReport.objects.all()
        authorization = Authorization()
        authentication = ApiKeyAuthentication()

        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']

    filtering = {
        "shout" : ALL_WITH_RELATIONS,
        "reporter" : ALL_WITH_RELATIONS,
    }
