from django.db import models

# Create your models here.

class Debt(models.Model):
    toWhom = models.CharField(max_length=50)
    howMuch = models.FloatField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.toWhom