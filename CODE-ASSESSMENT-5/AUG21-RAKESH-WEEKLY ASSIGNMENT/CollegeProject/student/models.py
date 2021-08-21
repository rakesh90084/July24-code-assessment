from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    admission_no=models.IntegerField()
    roll_no=models.IntegerField()
    college=models.CharField(max_length=100)
    parent_name=models.CharField(max_length=50)
   
