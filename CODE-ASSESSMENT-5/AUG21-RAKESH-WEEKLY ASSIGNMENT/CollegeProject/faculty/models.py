from django.db import models

# Create your models here.
class Faculty(models.Model):
    faculty_code=models.IntegerField()
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    mobile_number=models.BigIntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
   
