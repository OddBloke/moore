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
        return self.name if self.name else "Unnamed Group"


class WrestlingTeam(Group, WrestlingEntity):

    pass


class Wrestler(WrestlingEntity):

    pass
