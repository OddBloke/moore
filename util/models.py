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

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver

class Review(models.Model):

    reviewed_by = models.ForeignKey(User, null=True, blank=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField()

    @property
    def reviewed(self):
        return self.reviewed_at == self.updated_at

    class Meta:
        abstract = True


@receiver(pre_save)
def review_pre_save_handler(instance, *args, **kwargs):
    if isinstance(instance, Review):
        now = datetime.now()
        instance.updated_at = now
        if instance.reviewed_at is None and instance.reviewed_by is not None:
            # First review
            instance.reviewed_at = now

        if hasattr(instance, '_old_review_time'):
            # We've previously had a review
            if instance._old_review_time != instance.reviewed_at:
                # We've had a new review
                instance.reviewed_at = now

        if instance.reviewed_at is not None:
            # Store the old review time
            instance._old_review_time = instance.reviewed_at


@receiver(m2m_changed)
def review_m2m_handler(instance, *args, **kwargs):
    if isinstance(instance, Review):
        instance.save()
