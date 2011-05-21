from django.db import models


class Promotion(models.Model):

    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    parent = models.ForeignKey("self", null=True, blank=True)
