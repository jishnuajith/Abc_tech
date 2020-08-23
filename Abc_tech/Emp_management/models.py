from django.db import models
import random

DEFAULT = ['Male', 'Female']

rand = random.shuffle(DEFAULT)


# Create your models here.

class Employee(models.Model):
    empName = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.BigIntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='static/', default='static/avatar.png')
    address = models.TextField()



    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.empName
