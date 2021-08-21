from rest_framework import serializers
from faculty.models import Faculty

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=('faculty_code','name','department','address','mobile_number','username','password')