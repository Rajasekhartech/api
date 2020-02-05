from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length= 10)
    id = models.IntegerField(primary_key= True)

    def __str__(self):
        return self.all


