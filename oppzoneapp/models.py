from django.db import models

# Create your models here.

class DataPoint(models.Model):
    CTN = models.CharField(max_length=12)
    tractName = models.CharField(max_length=50)
    countyName = models.CharField(max_length=50)
    stateName = models.CharField(max_length=50)
    population = models.IntegerField()
    MHI = models.IntegerField()
    homeValue = models.IntegerField()
    poverty = models.FloatField()
    bachelors = models.FloatField()
    state = models.IntegerField()
    county = models.IntegerField()
    tract = models.IntegerField()

    def __str__(self):
        return self.CTN
