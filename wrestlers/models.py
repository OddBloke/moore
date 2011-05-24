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
from review.models import Review


class GroupManager(models.Manager):

    def filter_wrestlers(self, l):
        return self.filter(wrestlers=Wrestler.objects.filter(id__in=[w.id for w in l]))


class WrestlingEntity(Review):

    name = models.CharField(max_length=128)
    bio = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.name


class Group(models.Model):

    objects = GroupManager()

    wrestlers = models.ManyToManyField("Persona")
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name if self.name else ", ".join([w.name for w in self.wrestlers])


class WrestlingTeam(WrestlingEntity, Group):

    pass


class Wrestler(Review):

    name = models.CharField(max_length=128)
    bio = models.TextField(blank=True,null=True)
    born_when = models.DateField(null=True, blank=True)
    born_location = models.CharField(max_length=128,blank=True,null=True)
    trained_by = models.ManyToManyField('Wrestler',blank=True)

    def __unicode__(self):
        return self.name


class Persona(WrestlingEntity):

    wrestler = models.ForeignKey(Wrestler)
    billed_height = models.DecimalField(null=True, blank=True,help_text="in metres",decimal_places=2,max_digits=10)
    billed_weight = models.IntegerField(null=True, blank=True,help_text="in kilograms")
    debut = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.name
