from django.contrib.auth.models import User
from django.db import models

from promotions.models import Promotion
from wrestlers.models import WrestlingEntity


class Review(models.Model):

    reviewed_by = models.ForeignKey(User, null=True, blank=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Card(models.Model):

    date = models.DateField()
    promotion = models.ForeignKey(Promotion)

    name = models.CharField(max_length=127, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.date)


class Match(Review):

    card = models.ForeignKey(Card)
    participants = models.ManyToManyField(WrestlingEntity)
    winner = models.ForeignKey(WrestlingEntity, related_name="won_matches",
                               null=True, blank=True)

    def vs_string(self):
        return " vs. ".join([p.name for p in self.participants.all()])

    def __unicode__(self):
        return "%s: %s" % (self.card.date, self.vs_string())
