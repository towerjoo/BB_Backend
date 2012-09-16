from django.db import models
from account.models import Account
from shout.models import Shout
from const.choices import ShoutNotificationStatusChoices

    
class ShoutNotification(models.Model):
    shout = models.ForeignKey(Shout, related_name="notficationShout")
    receiver = models.ForeignKey(Account, related_name="notificationReceiver")
    status = models.IntegerField(choices=ShoutNotificationStatusChoices.choices, default=ShoutNotificationStatusChoices.unread)

    def __unicode__(self):
        return "%s got a shout notfication:%s" % (self.receiver.user.username, self.shout.content[:20])

