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


class DataSource(models.Model):

    name = models.CharField(max_length=255, primary_key=True)


class SourcingDescription(models.Model):

    data_source = models.ForeignKey(DataSource)
    description = models.TextField()


class Sourced(models.Model):

    data_sources = models.ManyToManyField(SourcingDescription)

    class Meta:
        abstract = True
