from django.db import models


class Promotion(models.Model):

    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    parent = models.ForeignKey("self", null=True, blank=True)


class Title(models.Model):

    name = models.CharField(max_length=127)
    active_start_date = models.DateField()
    active_end_date = models.DateField()
