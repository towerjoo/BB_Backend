from django.db import models
from account.models import Account, ContactGroup
from venue.models import Venue
from const.choices import ShoutTypeChoices
from django.db.models.signals import post_save

class Shout(models.Model):
    author = models.ForeignKey(Account, related_name="shout-author")
    group =  models.ForeignKey(ContactGroup, related_name="shout-group", null=True, blank=True)
    venue = models.ForeignKey(Venue, related_name="shout-venue")
    content = models.CharField(max_length=180)
    photo = models.ImageField(upload_to="shouts/%Y/%m/%d", null=True, blank=True) 
    type = models.IntegerField(choices=ShoutTypeChoices.choices, default=ShoutTypeChoices.group)
    is_featured = models.BooleanField(default=False)
    time = models.DateTimeField()

    def __unicode__(self):
        if self.type == ShoutTypeChoices.group:
            return "%s shouts to group %s" % (self.author.user.username, self.group.name)
        else:
            return "%s shouts to billboard" % self.author.user.username

class ShoutComment(models.Model):
    shout = models.ForeignKey(Shout, related_name="commentShout")
    commenter = models.ForeignKey(Account, related_name="ShoutCommenter")
    content = models.CharField(max_length=100)
    comment_time = models.DateTimeField()

    def __unicode__(self):
        return "%s wrote a comment for shout %s" % (self.commenter.user.username, self.shout.content[:10])

class ShoutReport(models.Model):
    shout = models.ForeignKey(Shout, related_name="reportShout")
    reporter = models.ForeignKey(Account, related_name="ShoutReporter")
    content = models.CharField(max_length=100)
    report_time = models.DateTimeField()

    def __unicode__(self):
        return "%s reported shout %s" % (self.reporter.user.username, self.shout.content[:10])
    
def handle_shout_save(sender,instance, created, **kwargs):
    shout = instance
    import re
    if not created:
        return
    rx = re.compile(r"[^#]*#([^#]+)#")
    matches = rx.findall(shout.content)
    if matches:
        from trend.models import Trend
        for match in matches:
            Trend.objects.new_trend(match, shout.author)


    
post_save.connect(handle_shout_save, sender=Shout)
