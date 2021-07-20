from django.db import models

# Create your models here.


class Proccess(models.Model):

    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    # class Meta:
    #     verbose_name = ("test")
    #     verbose_name_plural = ("tests")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("test_detail", kwargs={"pk": self.pk})


class Current_task(models.Model):
    proc = models.ForeignKey(Proccess, on_delete=models.CASCADE)
    start_time = models.DateTimeField(name="start time", auto_now_add=True)
    end_time = models.DateTimeField(name="end time")
    store = models.IntegerField(name="store_number")
    mode = models.CharField(max_length=10)

    def __str__(self):
        return self.store
