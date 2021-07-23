from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Worksheet(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    date = models.DateField(name="date", auto_now_add=True)

    class Meta:
        verbose_name = ("Worksheet")
        verbose_name_plural = ("Worksheets")

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse("Worksheet_detail", kwargs={"pk": self.pk})


class Entry(models.Model):

    worksheet = models.ForeignKey(Worksheet, on_delete=models.CASCADE)
    start_time = models.TimeField(name="start_time", auto_now_add=True)
    operation = models.CharField(max_length=10)
    store = models.IntegerField(name="store", default=116)
    end_time = models.TimeField(name="end_time", default=timezone.now)

    class Meta:
        verbose_name = ("entry")
        verbose_name_plural = ("entries")

    def __str__(self):
        return self.operation

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"pk": self.pk})
