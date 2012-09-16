from django.db import models
from account.models import Account

class Trend(models.Model):
    topic = models.CharField(max_length=50)
    author = models.ForeignKey(Account, related_name="TopicAuthor")
    time = models.DateTimeField()

    def __unicode__(self):
        return "%s tweet on topic %s" % (self.author.user.username, self.topic)


