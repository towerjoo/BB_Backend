from django.db import models
from account.models import Account
from datetime import datetime 
from django.utils.timezone import utc

class TrendManager(models.Manager):
    def new_trend(self, topic, author):
        rec = self.model(topic=topic, author=author)
        rec.time = datetime.utcnow().replace(tzinfo=utc)
        rec.save()

class Trend(models.Model):
    topic = models.CharField(max_length=50)
    author = models.ForeignKey(Account, related_name="TopicAuthor")
    time = models.DateTimeField()

    objects = TrendManager()

    def __unicode__(self):
        return "%s tweet on topic %s" % (self.author.user.username, self.topic)


