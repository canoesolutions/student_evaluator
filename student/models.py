from enum import unique
from django.db import models

# Create your models here.
class Student_Details(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    college_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    mobile_num = models.CharField(max_length=10, unique=True)
    email_id = models.EmailField(max_length=254, unique=True)
    hometown = models.CharField(max_length=20)
    

    def __str__(self):
        return self.first_name
    