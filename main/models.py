from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from datetime import datetime, timedelta
from time import strftime
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import lazy
from main.choices import OPERATION_CHOICES, STORE_CHOICES


class Worksheet(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="worksheet",
        null=True
    )
    name = models.CharField(max_length=20)
    date = models.DateField(name="date", auto_now_add=True)
    complete = models.BooleanField(db_column="Completed", default=False)

    stores = STORE_CHOICES

    class Meta:
        verbose_name = _("Worksheet")
        verbose_name_plural = _("Worksheets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tracker", kwargs={"id": self.pk})

    operations = OPERATION_CHOICES


class Entry(models.Model):

    # TODO validate start and end times. End time cannot be lower than start time.
    worksheet = models.ForeignKey(Worksheet, on_delete=models.CASCADE)
    start_time = models.TimeField(_("Start Time"))
    operation = models.CharField(
        _("Operation"), choices=OPERATION_CHOICES, max_length=50)
    store = models.IntegerField(_("Store"), choices=STORE_CHOICES, default=116)
    end_time = models.TimeField(_("End time"), null=True, blank=True)

    class Meta:
        verbose_name = _("entry")
        verbose_name_plural = _("entries")

    def __str__(self):

        day = self.worksheet.date.strftime('%A')
        start = self.start_time.strftime('%I:%M:%S %p')
        if self.end_time == None:
            end = "None"
        else:
            end = self.end_time.strftime('%I:%M:%S %p')

        return day + "-" + str(self.store) + "-" + self.operation + "-" + start + "-" + end

    def get_absolute_url(self):
        return reverse("tracker", kwargs={"id": self.worksheet.pk})
