from django.db import models

# Create your models here.
class Employee(models.Model):
   
    Employee_code=models.IntegerField()
    name=models.CharField(max_length=150)
    address=models.CharField(max_length=120)
    mobile_no=models.BigIntegerField()
    salary=models.IntegerField()
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)