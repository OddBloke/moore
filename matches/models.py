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

from promotions.models import Promotion
from util.models import Review
from wrestlers.models import WrestlingEntity


class Card(models.Model):

    date = models.DateField()
    promotion = models.ForeignKey(Promotion)

    name = models.CharField(max_length=127, null=True, blank=True)

    def next_order_number(self):
        nxt = 1
        for m in self.match_set.order_by('order'):
            if m.order != nxt:
                return nxt
            nxt += 1
        return nxt

    def __unicode__(self):
        return unicode(self.date)


class Match(Review):

    order = models.IntegerField()
    card = models.ForeignKey(Card)
    participants = models.ManyToManyField(WrestlingEntity)
    winner = models.ForeignKey(WrestlingEntity, related_name="won_matches",
                               null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order is None:
            self.order = self.card.next_order_number()
        super(Match, self).save(*args, **kwargs)

    def vs_string(self):
        return " vs. ".join([p.name for p in self.participants.all()])

    def __unicode__(self):
        return "%s: %s" % (self.card.date, self.vs_string())
