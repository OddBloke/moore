from django.db import models

from wrestlers.models import WrestlingEntity


class Card(models.Model):

    date = models.DateField()

    def __unicode__(self):
        return unicode(self.date)


class Match(models.Model):

    card = models.ForeignKey(Card)
    participants = models.ManyToManyField(WrestlingEntity)
    winner = models.ForeignKey(WrestlingEntity, related_name="won_matches",
                               null=True, blank=True)

    def __unicode__(self):
        return " vs. ".join([p.name for p in self.participants.all()])
