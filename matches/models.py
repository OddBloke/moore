from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver

from promotions.models import Promotion
from wrestlers.models import WrestlingEntity


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


class Card(models.Model):

    date = models.DateField()
    promotion = models.ForeignKey(Promotion)

    name = models.CharField(max_length=127, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.date)


class Match(Review):

    card = models.ForeignKey(Card)
    participants = models.ManyToManyField(WrestlingEntity)
    winner = models.ForeignKey(WrestlingEntity, related_name="won_matches",
                               null=True, blank=True)

    def vs_string(self):
        return " vs. ".join([p.name for p in self.participants.all()])

    def __unicode__(self):
        return "%s: %s" % (self.card.date, self.vs_string())
