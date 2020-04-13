from django.db import models

# Create your models here.

class NewDriverModel(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.title

class DriverDatabaseModel(models.Model):
    driver = models.CharField(max_length=32)
    passengers = models.CharField(max_length=32)