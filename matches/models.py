from django.db import models

from wrestlers.models import WrestlingEntity


class Card(models.Model):

    date = models.DateField()


class Match(models.Model):

    card = models.ForeignKey(Card)
    participants = models.ManyToManyField(WrestlingEntity)
    winner = models.ForeignKey(WrestlingEntity, related_name="won_matches",
                               null=True, blank=True)
