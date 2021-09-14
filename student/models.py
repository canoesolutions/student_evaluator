from enum import auto, unique
from django.db import models
from datetime import datetime, date

# Create your models here.

class Student_Details(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
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
        return self.first_name + ' ' + self.last_name


class Emotional_Intelligence(models.Model):
    ei_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student_Details', default="", on_delete=models.CASCADE)
    self_awareness = models.FloatField(null=True, default="")
    self_management = models.FloatField(null=True, default="")
    social_awareness = models.FloatField(null=True, default="")
    social_skills = models.FloatField(null=True, default="")
    emotional_intelligence = models.FloatField(null=True, default="")
    emotional_quotient = models.FloatField(null=True, default="")
    # created_by = models.CharField(max_length=20)
    # created_on = models.DateField(blank=True, null=True)
    # updated_by = models.CharField(max_length=20)
    # updated_on = models.DateField(blank=True, null=True)


class Intellectual_Capacity(models.Model):
    ic_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student_Details, default="", on_delete=models.CASCADE)
    clear_thinking = models.IntegerField(null=True, default="")
    observational_ability = models.IntegerField(null=True, default="")
    reasoning_ability = models.IntegerField(null=True, default="")
    critical_reasoning = models.IntegerField(null=True, default="")
    abstract_reasoning = models.IntegerField(null=True, default="")
    intelligence_quotient = models.IntegerField(null=True, default="")
    # created_by = models.CharField(max_length=20)
    # created_on = models.DateField(blank=True, null=True)
    # updated_by = models.CharField(max_length=20)
    # updated_on = models.DateField(blank=True, null=True)


class Personal_Test(models.Model):
    pt_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student_Details, default="", on_delete=models.CASCADE)
    initiative = models.IntegerField(null=True, default="")
    sees_act = models.IntegerField(null=True, default="")
    persistence = models.IntegerField(null=True, default="")
    info_seek = models.IntegerField(null=True, default="")
    concern_high = models.IntegerField(null=True, default="")
    commitment_work = models.IntegerField(null=True, default="")
    efficiency_orientation = models.IntegerField(null=True, default="")
    systematic_planning = models.IntegerField(null=True, default="")
    problem_solving = models.IntegerField(null=True, default="")
    self_confidence = models.IntegerField(null=True, default="")
    assertiveness = models.IntegerField(null=True, default="")
    persuasion = models.IntegerField(null=True, default="")
    use_of_influence = models.IntegerField(null=True, default="")
    average_competency = models.FloatField(null=True, default="")
    correction_factor = models.IntegerField(null=True, default="")
    # created_by = models.CharField(max_length=20)
    # created_on = models.DateField(blank=True, null=True)
    # updated_by = models.CharField(max_length=20)
    # updated_on = models.DateField(blank=True, null=True)
    
    
class Meta_Cognitive_Test(models.Model):
    mct_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student_Details, default="", on_delete=models.CASCADE)
    planning_skill = models.IntegerField(null=True, default="")
    implementation_skill = models.IntegerField(null=True, default="")
    monitoring_skill = models.IntegerField(null=True, default="")
    evalauation_skill = models.IntegerField(null=True, default="")
    # created_by = models.CharField(max_length=20)
    # created_on = models.DateField(blank=True, null=True)
    # updated_by = models.CharField(max_length=20)
    # updated_on = models.DateField(blank=True, null=True)
    