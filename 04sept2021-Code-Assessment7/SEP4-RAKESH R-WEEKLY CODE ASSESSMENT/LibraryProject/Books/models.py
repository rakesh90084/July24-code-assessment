from django.db import models

# Create your models here.
class Books(models.Model):
   
    book_name=models.CharField(max_length=100)
    author=models.CharField(max_length=150)
    description=models.CharField(max_length=120)
    price=models.IntegerField()
    category=models.CharField(max_length=150)

