from django.db import models

# Create your models here.
class Patients(models.Model):
    Patient_ID = models.IntegerField()
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Disease = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)

def __str__(self):
    return self.Name