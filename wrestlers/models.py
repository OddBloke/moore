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

    def filter_members(self, l):
        return self.filter(members=Individual.objects.filter(id__in=[w.id for w in l]))


class WrestlingEntity(models.Model):

    bio = models.TextField(blank=True,null=True)


class Group(WrestlingEntity):

    objects = GroupManager()

    members = models.ManyToManyField("Persona")
    group_name = models.CharField(max_length=128, null=True, blank=True)

    @property
    def name(self):
        return self.group_name

    def __unicode__(self):
        if self.group_name is not None and self.group_name != '':
            return self.group_name
        else:
            names = [unicode(w) for w in self.wrestlers.all()]
            return "%s & %s" % (', '.join(names[:-1]), names[-1])


class Individual(models.Model):

    name = models.CharField(max_length=128)
    bio = models.TextField(blank=True,null=True)
    born_when = models.DateField(null=True, blank=True)
    born_location = models.CharField(max_length=128,blank=True,null=True)
    trained_by = models.ManyToManyField('Individual',blank=True)

    def __unicode__(self):
        return self.name


class Persona(WrestlingEntity):

    billed_name = models.CharField(max_length=128)
    individual = models.ForeignKey(Individual)
    billed_height = models.DecimalField(null=True, blank=True,help_text="in metres",decimal_places=2,max_digits=10)
    billed_weight = models.IntegerField(null=True, blank=True,help_text="in kilograms")
    debut = models.DateField(null=True, blank=True)

    @property
    def name(self):
        return self.billed_name

    def __unicode__(self):
        return self.billed_name
