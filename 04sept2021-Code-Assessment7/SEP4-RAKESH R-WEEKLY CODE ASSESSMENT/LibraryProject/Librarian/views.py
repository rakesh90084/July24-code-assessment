from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Librarian.serializers import LibrarianSerializer
from Librarian.models import Librarian
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")

    getlibrariancode=request.POST.get("newlibrariancode")    
    getname=request.POST.get("newname")
    getaddress=request.POST.get("newaddress")
    getmobileno=request.POST.get("newmobileno")
    getpincode=request.POST.get("newpincode")
    getemailid=request.POST.get("newemailid")
    getusername=request.POST.get("newusername")
    getpassword=request.POST.get("newpassword")
    
    mydata={'librarian_code':getlibrariancode,'name':getname,'address':getaddress,'mobile_no':getmobileno,'pincode':getpincode,'email_id':getemailid,'username':getusername,'password':getpassword}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/Librarian/viewlibrarian/" + getId
    requests.put(ApiLink,data=jsondata)
    return redirect(viewall)
    # return HttpResponse("Data updated successfully")
@csrf_exempt
def delete_data_read(request):
   
    getId=request.POST.get("newid")

   
    ApiLink="http://127.0.0.1:8000/Librarian/viewlibrarian/" + getId
    requests.delete(ApiLink)
    return redirect(viewall)
    # return HttpResponse("Data deleted successfully")    
@csrf_exempt
def searchapi(request):
    try:
        getlibrariancode=request.POST.get("librarian_code")
        getlibrariancodes=Librarian.objects.filter(librarian_code=getlibrariancode)
        librarian_serialize=LibrarianSerializer(getlibrariancodes,many=True)
        return render(request,"search_lib.html",{"data":librarian_serialize.data})
    except:   
        return HttpResponse("Invalid Librarian code",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def update_search_api(request):
    try:
        getlibrariancode=request.POST.get("librarian_code")
        getlibrariancodes=Librarian.objects.filter(librarian_code=getlibrariancode)
        librarian_serialize=LibrarianSerializer(getlibrariancodes,many=True)
        return render(request,"update_lib.html",{"data":librarian_serialize.data})
    except:   
        return HttpResponse("Invalid Librarian code",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def delete_search_api(request):
    try:
        getlibrariancode=request.POST.get("librarian_code")
        getlibrariancodes=Librarian.objects.filter(librarian_code=getlibrariancode)
        librarian_serialize=LibrarianSerializer(getlibrariancodes,many=True)
        return render(request,"delete_lib.html",{"data":librarian_serialize.data})
    except:   
        return HttpResponse("Invalid librarian code")
def register(request):
    return render(request,'register_lib.html')
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/Librarian/viewall/").json()
    return render(request,'view_lib.html',{"data":fetchdata})
def update(request):
    return render(request,'update_lib.html') 
def delete(request):
    return render(request,'delete_lib.html')  
def search_librarian(request):
    return render(request,'search_lib.html') 
def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact_lib.html') 
def loginview(request):
    return render(request,"login.html") 
@csrf_exempt
def login_check(request):
    # username=request.POST.get("username")
    # password=request.POST.get("password")

    # try:
    username=request.POST.get("username")
    password=request.POST.get("password")
    getlibrarian=Librarian.objects.filter(username=username,password=password)
    librarian_serializer=LibrarianSerializer(getlibrarian,many=True)
    if(librarian_serializer.data):
        for i in librarian_serializer.data:
            x=i["name"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        # return render(request,"home.html")
        return render(request,'view_lib.html',{"data":librarian_serializer.data})
    else:
        return HttpResponse("Invalid Credentials")                              
@csrf_exempt
def librarian_details(request,fetchid):
    try:
        librarian=Librarian.objects.get(id=fetchid)
        if(request.method=="GET"):
            librarian_serializer=LibrarianSerializer(librarian)
            return JsonResponse(librarian_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            librarian.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            librarian_serialize=LibrarianSerializer(librarian,data=mydata)
            if(librarian_serialize.is_valid()):
                librarian_serialize.save()
                return JsonResponse(librarian_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(librarian_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)
    
        


@csrf_exempt
def librarian_list(request):
    if(request.method=="GET"):
        librarian=Librarian.objects.all()
        librarian_serializer=LibrarianSerializer(librarian,many=True)
        return JsonResponse(librarian_serializer.data,safe=False)

@csrf_exempt
def librarianPage(request):
    if(request.method=="POST"):
        librarian_serialize=LibrarianSerializer(data=request.POST)
        if(librarian_serialize.is_valid()):
            librarian_serialize.save()
            return redirect(viewall)
            # return JsonResponse(Librarian_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)    
      
    else:
        return HttpResponse("No GET method Allowed",status=status.HTTP_404_NOT_FOUND)

