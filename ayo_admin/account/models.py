from django.db import models
from django.contrib.auth.models import User
from const.choices import AccountTypeChoices

class AccountManager(models.Manager):
    pass

class Account(models.Model):
    user = models.ForeignKey(User, related_name="user")
    type = models.IntegerField(choices=AccountTypeChoices.choices, default=AccountTypeChoices.individual)
    icon = models.ImageField(upload_to="icons/%Y/%m/%d", null=True, blank=True) 
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    facebook_id = models.CharField(max_length=100, null=True, blank=True)
    facebook_access_token = models.CharField(max_length=100, null=True, blank=True)
    api_access_token = models.CharField(max_length=100, null=True, blank=True)
    is_facebook_account = models.BooleanField(default=True)
    register_time = models.DateTimeField(auto_now_add=True)
    last_login_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s(%s)" % (self.user.username, AccountTypeChoices.get_value(self.type))

class FollowRelation(models.Model):
    follower = models.ForeignKey(User, related_name="follower")
    followee = models.ForeignKey(User, related_name="followee")
    follow_time = models.DateTimeField()

    def __unicode__(self):
        return "%s is following %s" % (self.follower.user.username, self.followee.user.username)


class ContactGroup(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(Account, related_name="ContactGroupOwner")
    members = models.TextField(default="[]")    # serilized data
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s's %s contact group" % (self.owner.user.username,self.name)
