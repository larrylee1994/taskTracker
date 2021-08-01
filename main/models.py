from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from datetime import datetime, timedelta
from time import strftime
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Worksheet(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="worksheet", null=True)
    name = models.CharField(max_length=20)
    date = models.DateField(name="date", auto_now_add=True)

    stores = [
        {"name": 'Orlando',  "number": 116},
        {"name": 'LBV',      "number": 167},
        {"name": 'Vineland', "number": 215},
        {"name": 'Footwear', "number": 254},
        {"name": 'Youth',    "number": 279},
        {"name": 'Disney',   "number": 517},
    ]

    class Meta:
        verbose_name = _("Worksheet")
        verbose_name_plural = _("Worksheets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tracker", kwargs={"id": self.pk})
        # return "tracker/%i" % self.pk
    
    def get_operations(self):
        op = Operation.objects.all()
        list = []
        for item in op:
            list.append({"name":item.name, "desc":item.description})
        return list

    # DEMO user defined operations
    operations = get_operations


class Entry(models.Model):

    worksheet = models.ForeignKey(Worksheet, on_delete=models.CASCADE)
    start_time = models.TimeField(name="start_time", null=True, blank=True)
    operation = models.CharField(name="operation", max_length=10)
    store = models.IntegerField(name="store", default=116)
    end_time = models.TimeField(name="end_time", null=True, blank=True)

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

class Operation(models.Model):

    name = models.CharField(name="name", max_length=30)
    description = models.CharField(name="description", max_length=30)

    class Meta:
        verbose_name = _("Operation")
        verbose_name_plural = _("Operations")

    def __str__(self):
        return self.name
