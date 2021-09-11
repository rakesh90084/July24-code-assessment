from rest_framework import serializers
from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('id','Employee_code','name','address','mobile_no','salary','username','password')