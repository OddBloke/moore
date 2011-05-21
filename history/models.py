from django.core.exceptions import ValidationError
from django.db import models


class HistorisedObjectManager(models.Manager):

    def get_current(self):
        return self.get(end_date__isnull=True)


class HistorisedObject(models.Model):

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    objects = HistorisedObjectManager()

    def clean(self):
        name = self._meta.object_name
        parent_name = self.obj._meta.object_name
        if self.end_date is not None and self.start_date > self.end_date:
            raise ValidationError("Start date of %(name)s after end date of"
                                  " %(name)s." % {'name': name})
        self.obj.clean_fields()
        if self.start_date < self.obj.start_date:
            raise ValidationError("Start date of %s before start date of %s."
                                  % (name, parent_name))
        if (self.obj.end_date is not None
                and self.start_date > self.obj.end_date):
            raise ValidationError("Start date of %s after end date of %s."
                                  % (name, parent_name))
        if (self.obj.end_date is not None
                and self.end_date is not None
                and self.end_date > self.obj.end_date):
            raise ValidationError("End date of %s after end date of %s."
                                  % (name, parent_name))

    def save(self, *args, **kwargs):
        self.full_clean()
        super(HistorisedObject, self).save(*args, **kwargs)

    class Meta:
        abstract = True
