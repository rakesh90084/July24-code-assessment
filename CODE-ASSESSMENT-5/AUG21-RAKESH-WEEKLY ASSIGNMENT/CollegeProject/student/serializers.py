from rest_framework import serializers
from student.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('name','admission_no','roll_no','college','parent_name')