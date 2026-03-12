from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    age = models.CharField(max_length=100)
    monthly_salary = models.CharField(max_length=10000)