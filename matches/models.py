from django.db import models

from promotions.models import Promotion
from util.models import Review
from wrestlers.models import WrestlingEntity


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
