from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from faculty.serializers import FacultySerializer
from faculty.models import Faculty
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def register_faculty(request):
    return render(request,'register_faculty.html')
def login_faculty(request):
    return render(request,'login.html')    
@csrf_exempt    
def faculty_fetch(request,fcode):
    try:
        faculty=Faculty.objects.get(faculty_code=fcode)
        if(request.method=="GET"):
            faculty_serializer=FacultySerializer(faculty)
            return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
    except faculty.DoesNotExist:
        return HttpResponse("Invalid Faculty code ",status=status.HTTP_404_PAGE_NOT_FOUND)        
@csrf_exempt
def faculty_details(request,fetchid):
    try:
        faculty=Faculty.objects.get(id=fetchid)
        if(request.method=="GET"):
            faculty_serializer=FacultySerializer(faculty)
            return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            faculty.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            faculty_serializer=FacultySerializer(faculty,data=mydata)
            if(faculty_serializer.is_valid()) :
                faculty_serializer.save()  
                return JsonResponse(faculty_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(faculty_serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)    
@csrf_exempt
def faculty_list(request):
    if(request.method=="GET"):
        faculty=Faculty.objects.all()
        faculty_serializer=FacultySerializer(faculty,many=True)
        return JsonResponse(faculty_serializer.data,safe=False)    
@csrf_exempt
def facultyaddpage(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        faculty_serialize=FacultySerializer(data=mydata)
        if(faculty_serialize.is_valid()):
            faculty_serialize.save()
            return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST) 
    else:
        return HttpResponse("No get method allowed",status=status.HTTP_404_PAGE_NOT_FOUND)                   
                  

