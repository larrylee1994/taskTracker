from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from datetime import datetime, timedelta
from time import strftime

# Create your models here.


class Worksheet(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="worksheet", null=True)
    name = models.CharField(max_length=20)
    date = models.DateField(name="date", auto_now_add=True)

    # TODO: implement operation.value, and operation.desciption
    operations = [
        "REC",
        "BACK",
        "PROC",
        "SCAN",
        "R_PICK",
        "B_PICK",
        "S_PICK",
        "DEL",
        "LOAD",
        "Break",
        "Lunch",
        "Cleaning",
    ]

    stores = [
        116,
        167,
        215,
        254,
        279,
        517,
    ]

    class Meta:
        verbose_name = ("Worksheet")
        verbose_name_plural = ("Worksheets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("Worksheet_detail", kwargs={"pk": self.pk})
        return "tracker/%i" % self.pk

class Entry(models.Model):

    worksheet = models.ForeignKey(Worksheet, on_delete=models.CASCADE)
    start_time = models.TimeField(name="start_time", null=True, blank=True)
    operation = models.CharField(name="operation", max_length=10)
    store = models.IntegerField(name="store", default=116)
    end_time = models.TimeField(name="end_time", null=True, blank=True)

    class Meta:
        verbose_name = ("entry")
        verbose_name_plural = ("entries")

    def __str__(self):

        day = self.worksheet.date.strftime('%A')
        start = self.start_time.strftime('%I:%M:%S %p')
        name = self.worksheet.name
        if self.end_time == None:
            end = "None"
        else:
            end = self.end_time.strftime('%I:%M:%S %p')

        return name + "-" + day + "-" + str(self.store) + "-" + self.operation + "-" + start + "-" + end
    
    def get_absolute_url(self):
        # return reverse("entry_detail", kwargs={"pk": self.pk})
        return "tracker/%i" % self.worksheet.pk
