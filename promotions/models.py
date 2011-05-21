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

from django.core.exceptions import ValidationError
from django.db import models


class PromotionName(models.Model):

    promotion = models.ForeignKey("Promotion", related_name="names")
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def clean(self):
        if self.end_date is not None and self.start_date > self.end_date:
            raise ValidationError("Start date after end date.")
        self.promotion.clean_fields()
        if self.start_date < self.promotion.start_date:
            raise ValidationError("Start date of name before start date of"
                                  " promotion.")
        if (self.promotion.end_date is not None
                and self.start_date > self.promotion.end_date):
            raise ValidationError("Start date of name after end date of"
                                  " promotion.")
        if (self.promotion.end_date is not None
                and self.end_date is not None
                and self.end_date > self.promotion.end_date):
            raise ValidationError("End date of name after end date of"
                                  " promotion.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(PromotionName, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Promotion(models.Model):

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def name(self):
        return self.names.get(end_date__isnull=True).name

    def __unicode__(self):
        return self.name()


class Title(models.Model):

    name = models.CharField(max_length=127)
    active_start_date = models.DateField()
    active_end_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.name
