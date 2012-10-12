from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication, Authentication

from django.db import models
from tastypie.models import create_api_key
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from account.models import Account, FollowRelation, ContactGroup


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        excludes = ["email", "password"]
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        excludes = ["password", "is_staff", "is_active", "is_superuser", "groups", "user_permissions", ]
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get', 'put']
        filtering = {
            "username" : ALL,
        }

class AccountResource(ModelResource):
    user = fields.ForeignKey(UserResource, "user")
    class Meta:
        queryset = Account.objects.all()
        authorization = Authorization()
        authentication = ApiKeyAuthentication()

        list_allowed_methods = ['get']
        detail_allowed_methods = ['get', 'put']

        filtering = {
            "id" : ALL,
            "user" : ALL_WITH_RELATIONS,
            "gender" : ALL,
            "type" : ALL,
        }

class FollowRelationResource(ModelResource):
    follower = fields.ForeignKey(AccountResource, "follower")
    followee = fields.ForeignKey(AccountResource, "followee")
    class Meta:
        queryset = FollowRelation.objects.all()
        authorization = Authorization()
        authentication = ApiKeyAuthentication()

        list_allowed_methods = ['get']
        detail_allowed_methods = ['get', 'put', 'delete']
        filtering = {
            "follower" : ALL_WITH_RELATIONS,
            "followee" : ALL_WITH_RELATIONS,
        }

    def obj_create(self, bundle, request=None, **kwargs):
        member = Account.objects.get_account_from_user(request.user)
        return super(FollowRelationResource, self).obj_create(bundle, request, follower=member)

    def apply_authorization_limits(self, request, object_list):
        member = Account.objects.get_account_from_user(request.user)
        ret = object_list.filter(follower=member)
        return ret

class ContactGroupResource(ModelResource):
    owner = fields.ForeignKey(AccountResource, "owner")
    class Meta:
        queryset = ContactGroup.objects.all()
        authorization = Authorization()
        authentication = ApiKeyAuthentication()

        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        filtering = {
            "owner" : ALL_WITH_RELATIONS,
            "name" : ALL,
        }

    def obj_create(self, bundle, request=None, **kwargs):
        member = Account.objects.get_account_from_user(request.user)
        return super(ContactGroupResource, self).obj_create(bundle, request, owner=member)

    def apply_authorization_limits(self, request, object_list):
        member = Account.objects.get_account_from_user(request.user)
        ret = object_list.filter(owner=member)
        return ret
