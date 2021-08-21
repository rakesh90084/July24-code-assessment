from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from student.serializers import StudentSerializer
from student.models import Student
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def register(request):
    return render(request,'register.html')
@csrf_exempt    
def admission(request,admno):
    try:
        student=Student.objects.get(admission_no=admno)
        if(request.method=="GET"):
            student_serializer=StudentSerializer(student)
            return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
    except student.DoesNotExist:
        return HttpResponse("Invalid Id ",status=status.HTTP_404_PAGE_NOT_FOUND)        
@csrf_exempt
def student_details(request,fetchid):
    try:
        student=Student.objects.get(id=fetchid)
        if(request.method=="GET"):
            student_serializer=StudentSerializer(student)
            return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            student.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            student_serializer=StudentSerializer(student,data=mydata)
            if(student_serializer.is_valid()) :
                student_serializer.save()  
                return JsonResponse(student_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(student_serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
    except Student.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)    
@csrf_exempt
def student_list(request):
    if(request.method=="GET"):
        student=Student.objects.all()
        student_serializer=StudentSerializer(student,many=True)
        return JsonResponse(student_serializer.data,safe=False)    
@csrf_exempt
def studentaddpage(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        student_serialize=StudentSerializer(data=mydata)
        if(student_serialize.is_valid()):
            student_serialize.save()
            return JsonResponse(student_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST) 
    else:
        return HttpResponse("No get method allowed",status=status.HTTP_404_PAGE_NOT_FOUND)                   
