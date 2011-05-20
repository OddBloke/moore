from django.db import models


class GroupManager(models.Manager):

    def filter_wrestlers(self, l):
        return self.filter(wrestlers=Wrestler.objects.filter(id__in=[w.id for w in l]))

class Group(models.Model):

    objects = GroupManager()

    wrestlers = models.ManyToManyField("Wrestler")
    name = models.CharField(max_length=128)


class Wrestler(models.Model):

    name = models.CharField(max_length=128)
