from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class User(models.Model):

    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})


class Worksheet(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(name="date", auto_now_add=True)

    class Meta:
        verbose_name = ("Worksheet")
        verbose_name_plural = ("Worksheets")

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse("Worksheet_detail", kwargs={"pk": self.pk})


class Entry(models.Model):

    worksheet = models.ForeignKey(Worksheet, on_delete=models.CASCADE)
    start_time = models.DateTimeField(name="start_time", auto_now_add=True)
    operation = models.CharField(max_length=10)
    store = models.IntegerField(name="store", default=116)
    end_time = models.DateTimeField(name="end_time", default=timezone.now)

    class Meta:
        verbose_name = ("entry")
        verbose_name_plural = ("entries")

    def __str__(self):
        return self.operation

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"pk": self.pk})
