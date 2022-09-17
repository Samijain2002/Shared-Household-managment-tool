from django.db import models
from django.utils import timezone
# Create your models here.

class Tiffin(models.Model):
    shifts = (("1", "Morning"), ("2", "Night"))
    sami = models.IntegerField(default=0)
    utsi = models.IntegerField(default=0)
    vanshi = models.IntegerField(default=0)
    meetu = models.IntegerField(default=0)
    shift = models.CharField(max_length = 1, choices = shifts, default="1")
    today_day = models.DateField(default=timezone.now)
    def __str__(self):
        return f"{self.shift} {self.today_day}"  

class Water(models.Model):
    todays = models.DateField(default=timezone.now)
    count = models.IntegerField(default=1)
    def __str__(self) -> str:
        return str(self.todays) + " " + str(self.count)

class Maid(models.Model):
    payday = models.DateField(default=timezone.now)
    amount = models.IntegerField(default=0)
    class Meta:
        ordering= ["payday"]
    def __str__(self) -> str:
        return "Rs" + f"{self.amount} {self.payday}"

class Todo_list(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length = 100)
    added = models.DateField(default=timezone.now)
    def __str__(self):
        return self.title

    
    