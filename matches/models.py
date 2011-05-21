from django.contrib.auth.models import User
from django.db import models

from wrestlers.models import WrestlingEntity


class Review(models.Model):

    reviewed_by = models.ForeignKey(User)
    reviewed_at = models.DateTimeField()

    class Meta:
        abstract = True


class Card(models.Model):

    date = models.DateField()

    def __unicode__(self):
        return unicode(self.date)


class Match(Review):

    card = models.ForeignKey(Card)
    participants = models.ManyToManyField(WrestlingEntity)
    winner = models.ForeignKey(WrestlingEntity, related_name="won_matches",
                               null=True, blank=True)

    def __unicode__(self):
        return " vs. ".join([p.name for p in self.participants.all()])
