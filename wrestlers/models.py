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


class GroupManager(models.Manager):

    def filter_wrestlers(self, l):
        return self.filter(wrestlers=Wrestler.objects.filter(id__in=[w.id for w in l]))


class WrestlingEntity(models.Model):

    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Group(models.Model):

    objects = GroupManager()

    wrestlers = models.ManyToManyField("Wrestler")
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name if self.name else ", ".join([w.name for w in self.wrestlers])


class WrestlingTeam(WrestlingEntity, Group):

    pass


class Wrestler(WrestlingEntity):

    pass
