from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from time import strftime

# Create your models here.
class Worksheet(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="worksheet", null=True)
    name = models.CharField(max_length=20)
    date = models.DateField(name="date", auto_now_add=True)

    class Meta:
        verbose_name = ("Worksheet")
        verbose_name_plural = ("Worksheets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Worksheet_detail", kwargs={"pk": self.pk})

def default_end_time():
        now = datetime.now()
        start = now.replace(hour=18, minute=0, second=0, microsecond=0)
        return start if start > now else start + timedelta(seconds=600) 
class Entry(models.Model):

    worksheet = models.ForeignKey(Worksheet, on_delete=models.CASCADE)
    start_time = models.TimeField(name="start_time", auto_now_add=True)
    operation = models.CharField(max_length=10)
    store = models.IntegerField(name="store", default=116)
    end_time = models.TimeField(name="end_time", null=True, blank=True)

    class Meta:
        verbose_name = ("entry")
        verbose_name_plural = ("entries")

    def __str__(self):

        orig_start = str(self.start_time)
        start = datetime.strptime(orig_start, "%H:%M:%S.%f").strftime('%H:%M:%S')
        if self.end_time == None:
            end = "None"
        else:
            orig_end = str(self.end_time)
            end = datetime.strptime(orig_end, "%H:%M:%S.%f").strftime('%H:%M:%S')

        return start + " " + self.operation + " " + str(self.store) +" " + end

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"pk": self.pk})
