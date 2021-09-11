from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from employee.serializers import EmployeeSerializer
from employee.models import Employee
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth import logout
import requests

def signup(request):
    return render(request,'signup.html')

def update(request):
    return render(request,'update.html')   

def loginview(request):
    return render(request,"login.html")       

def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/employee/viewall/").json()
    return render(request,'view.html',{"data":fetchdata})


@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")

    getemployeecode=request.POST.get("newemployeecode")    
    getname=request.POST.get("newname")
    getaddress=request.POST.get("newaddress")
    getmobileno=request.POST.get("newmobileno")
    getsalary=request.POST.get("newsalary")
    getusername=request.POST.get("newusername")
    getpassword=request.POST.get("newpassword")
    
    mydata={'Employee_code':getemployeecode,'name':getname,'address':getaddress,'mobile_no':getmobileno,'salary':getsalary,'username':getusername,'password':getpassword}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/employee/viewemployee/" + getId
    requests.put(ApiLink,data=jsondata)
    return redirect(viewall)  

@csrf_exempt
def update_search_api(request):
    try:
        getemployeecode=request.POST.get("Employee_code")
        getemployeecodes=Employee.objects.filter(Employee_code=getemployeecode)
        employee_serialize=EmployeeSerializer(getemployeecodes,many=True)
        return render(request,"update.html",{"data":employee_serialize.data})
    except:   
        return HttpResponse("Invalid Employee code",status=status.HTTP_404_NOT_FOUND)      

@csrf_exempt
def employee_details(request,fetchid):
    try:
        employee=Employee.objects.get(id=fetchid)
        if(request.method=="GET"):
            employee_serializer=EmployeeSerializer(employee)
            return JsonResponse(employee_serializer.data,safe=False,status=status.HTTP_200_OK)
        
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            employee_serialize=EmployeeSerializer(employee,data=mydata)
            if(employee_serialize.is_valid()):
                employee_serialize.save()
                return JsonResponse(employee_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(employee_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    except Employee.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def employeePage(request):
    if(request.method=="POST"):
        employee_serialize=EmployeeSerializer(data=request.POST)
        if(employee_serialize.is_valid()):
            employee_serialize.save()
            return redirect(viewall)
            # return JsonResponse(employee_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)    
      
    else:
        return HttpResponse("No GET method Allowed",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def employee_list(request):
    if(request.method=="GET"):
        employee=Employee.objects.all()
        employee_serializer=EmployeeSerializer(employee,many=True)
        return JsonResponse(employee_serializer.data,safe=False)   

@csrf_exempt
def login_check(request):
    # username=request.POST.get("username")
    # password=request.POST.get("password")

    # try:
    username=request.POST.get("username")
    password=request.POST.get("password")
    getemployee=Employee.objects.filter(username=username,password=password)
    employee_serializer=EmployeeSerializer(getemployee,many=True)
    if(employee_serializer.data):
        for i in employee_serializer.data:
            x=i["name"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        # return render(request,"home.html")
        return render(request,'view.html',{"data":employee_serializer.data})
    else:
        return HttpResponse("Invalid Credentials")              
def logout(request):
        logout(request)
        template='login.html'
        return render(request,template) 
