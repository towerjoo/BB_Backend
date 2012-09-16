from django.db import models
from django.contrib.auth.models import User
from const.choices import AccountTypeChoices, AccountGenderChoices

class AccountManager(models.Manager):
    def facebook_connection(self, facebook_id, facebook_token, user_firstname, user_lastname, email, user_gender, type=AccountTypeChoices.individual):
        """need to check whether the username is unique
        """
        u = User.objects.filter(username=facebook_id)
        if u:
            acct = self.filter(user=u[0])
            if acct:
                acct.facebook_access_token = facebook_token #update access token
                acct.save()
                return True, acct
            return False, None

        user = User.objects.create_user(username=facebook_id, password=facebook_id, email=email)
        user.first_name = user_firstname
        user.last_name = user_lastname
        user.save()
        gender = AccountGenderChoices.male if user_gender.lower() == "male" else AccountGenderChoices.female
        rec = self.model(user=user, gender=gender, type=type, is_facebook_account=True, facebook_id=facebook_id, facebook_access_token=facebook_token)
        rec.save()
        return True, rec

    def new_user(self, username, user_firstname, user_lastname, password, email, user_gender, type=AccountTypeChoices.individual):
        """need to check whether the username is unique
        """
        u = User.objects.filter(username=username)
        if u:
            return False, None
        user = User.objects.create_user(username=username, password=password, email=email)
        user.first_name = user_firstname
        user.last_name = user_lastname
        user.save()
        gender = AccountGenderChoices.male if user_gender.lower() == "male" else AccountGenderChoices.female
        rec = self.model(user=user, gender=gender, type=type, is_facebook_account=False)
        rec.save()
        return True, rec



class Account(models.Model):
    user = models.ForeignKey(User, related_name="user")
    gender = models.IntegerField(choices=AccountGenderChoices.choices, default=AccountGenderChoices.male)
    type = models.IntegerField(choices=AccountTypeChoices.choices, default=AccountTypeChoices.individual)
    icon = models.ImageField(upload_to="icons/%Y/%m/%d", null=True, blank=True) 
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    facebook_id = models.CharField(max_length=100, null=True, blank=True)
    facebook_access_token = models.CharField(max_length=100, null=True, blank=True)
    is_facebook_account = models.BooleanField(default=True)
    register_time = models.DateTimeField(auto_now_add=True)
    last_login_time = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    def __unicode__(self):
        return "%s(%s)" % (self.user.username, AccountTypeChoices.get_value(self.type))

class FollowRelation(models.Model):
    follower = models.ForeignKey(User, related_name="follower")
    followee = models.ForeignKey(User, related_name="followee")
    follow_time = models.DateTimeField()

    def __unicode__(self):
        return "%s is following %s" % (self.follower.user, self.followee.user)


class ContactGroup(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(Account, related_name="ContactGroupOwner")
    members = models.TextField(default="[]")    # serilized data
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s's %s contact group" % (self.owner.user.username,self.name)
