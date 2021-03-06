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

from history.models import HistorisedObject


class PromotionName(HistorisedObject):

    obj = models.ForeignKey("Promotion", related_name="names")
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Promotion(models.Model):

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def name(self):
        recent = self.names.recent()
        if recent is not None:
            return recent.name
        return None

    def __unicode__(self):
        name = self.name()
        if name is None:
            return "<Unnamed>"
        return name


class TitlePromotion(HistorisedObject):

    obj = models.ForeignKey("Title", related_name="promotions")
    promotion = models.ForeignKey(Promotion)

    def __unicode__(self):
        return unicode(self.promotion)


class TitleName(HistorisedObject):

    obj = models.ForeignKey("Title", related_name="names")
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Title(models.Model):

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def name(self):
        recent = self.names.recent()
        if recent is not None:
            return recent.name
        return None

    def __unicode__(self):
        name = self.name()
        if name is None:
            return "<Unnamed>"
        return name
