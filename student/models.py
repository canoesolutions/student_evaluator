from enum import auto, unique
from django.db import models
from datetime import datetime, date

# Create your models here.

class Student_Details(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    college_name = models.CharField(max_length=50)
    student_year = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=20)    
    mobile_number = models.CharField(max_length=10, unique=True)
    email_id = models.EmailField(max_length=254, unique=True)
    hometown = models.CharField(max_length=20)
    test_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.first_name
    