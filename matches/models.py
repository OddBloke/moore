# moore - a wrestling database
# Copyright (C) 2011  Daniel Watkins
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from promotions.models import Promotion
from review.models import Review
from wrestlers.models import WrestlingEntity

class CardType(models.Model):
    """For example PPV, House Show, TV Episode"""
    name = models.CharField(max_length=127)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class Card(models.Model):
    """Represents a particular event for a wrestling promotion."""

    date = models.DateField()
    promotion = models.ManyToManyField(Promotion)
    card_type = models.ForeignKey(CardType)

    name = models.CharField(max_length=127, null=True, blank=True)

    def next_order_number(self):
        nxt = 1
        for m in self.cardevent_set.order_by('order'):
            if m.order != nxt:
                return nxt
            nxt += 1
        return nxt

    def __unicode__(self):
        return unicode(self.date)


class Role(models.Model):
    """A role that can be taken within a CardEvent."""

    description = models.CharField(max_length=255, primary_key=True)

    def __unicode__(self):
        return self.description


class Participation(models.Model):
    """The role which a WrestlingEntity takes within a CardEvent."""

    event = models.ForeignKey("CardEvent")
    participant = models.ForeignKey(WrestlingEntity)
    role = models.ForeignKey(Role)


# Hack to work around http://code.djangoproject.com/ticket/13757
@receiver(post_save, sender=Participation)
def participation_post_save_handler(instance, *args, **kwargs):
    instance.event.save()


class EventType(models.Model):
    """The type of an event (e.g. match, promo, interview)."""

    description = models.CharField(max_length=127, primary_key=True)

    def __unicode__(self):
        return self.description


class CardEvent(Review):
    """A particular event within a card."""

    order = models.IntegerField()
    card = models.ForeignKey(Card)
    participants = models.ManyToManyField(WrestlingEntity,
                                          through=Participation)
    event_type = models.ForeignKey(EventType)

    def save(self, *args, **kwargs):
        if self.order is None:
            self.order = self.card.next_order_number()
        super(CardEvent, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s #%d: %s: %s" % (self.card, self.order,
                                   self.event_type,
                                   ", ".join(self.participants.all()))


class MatchTypeAspect(models.Model):
    """An aspect of a match type (e.g. falls count anywhere)."""

    description = models.CharField(max_length=127, primary_key=True)

    def __unicode__(self):
        return self.description


class MatchType(models.Model):
    """A type of match, including various aspects."""

    description = models.CharField(max_length=127)
    aspects = models.ManyToManyField(MatchTypeAspect)

    def __unicode__(self):
        return self.description


class Match(CardEvent):
    """A match."""

    match_type = models.ForeignKey(MatchType)
    winner = models.ForeignKey(WrestlingEntity, related_name="won_matches",
                               null=True, blank=True)

    def add_competitor(self, wrestling_entity):
        role = Role.objects.get(description="Competitor")
        Participation.objects.create(event=self,
                                     participant=wrestling_entity,
                                     role=role)

    @property
    def competitor_list(self):
        return self.participants.filter(participation__role="Competitor")

    def save(self, *args, **kwargs):
        if self.winner is not None:
            if not self.winner.wrestlingentity_ptr in self.competitor_list:
                return
        self.event_type = EventType.objects.get(description="Match")
        if self.match_type_id is None:
            self.match_type = MatchType.objects.get(description="Standard")
        super(Match, self).save(*args, **kwargs)

    def vs_string(self):
        return " vs. ".join([p.name for p in self.participants.all()])

    def __unicode__(self):
        return "%s: %s" % (self.card.date, self.vs_string())
