from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Books.serializers import BooksSerializer
from Books.models import Books
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")

    getbookname=request.POST.get("newbookname")    
    getauthor=request.POST.get("newauthor")
    getdescription=request.POST.get("newdescription")
    getprice=request.POST.get("newprice")
    getcategory=request.POST.get("newcategory")
    
    mydata={'book_name':getbookname,'author':getauthor,'description':getdescription,'price':getprice,'category':getcategory}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/Books/viewbooks/" + getId
    requests.put(ApiLink,data=jsondata)
    return redirect(viewall)
    # return HttpResponse("Data updated successfully")
@csrf_exempt
def delete_data_read(request):
   
    getId=request.POST.get("newid")

   
    ApiLink="http://127.0.0.1:8000/Books/viewbooks/" + getId
    requests.delete(ApiLink)
    return redirect(viewall)
    # return HttpResponse("Data deleted successfully")    
@csrf_exempt
def searchapi(request):
    try:
        getbookname=request.POST.get("book_name")
        getbooknames=Books.objects.filter(book_name=getbookname)
        book_serialize=BooksSerializer(getbooknames,many=True)
        return render(request,"search.html",{"data":book_serialize.data})
    except:   
        return HttpResponse("Invalid Book name",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def update_search_api(request):
    try:
        getbookname=request.POST.get("book_name")
        getbooknames=Books.objects.filter(book_name=getbookname)
        book_serialize=BooksSerializer(getbooknames,many=True)
       
        return render(request,"update.html",{"data":book_serialize.data})
    except:   
        return HttpResponse("Invalid book name",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def delete_search_api(request):
    try:
        getbookname=request.POST.get("book_name")
        getbooknames=Books.objects.filter(book_name=getbookname)
        book_serialize=BooksSerializer(getbooknames,many=True)
        return render(request,"delete.html",{"data":book_serialize.data})
    except:   
        return HttpResponse("Invalid book name")
def register(request):
    return render(request,'register.html')
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/Books/viewall/").json()
    return render(request,'view.html',{"data":fetchdata})
def update(request):
    return render(request,'update.html') 
def delete(request):
    return render(request,'delete.html')  
def search_book(request):
    return render(request,'search.html') 
def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')                        
@csrf_exempt
def book_details(request,fetchid):
    try:
        book=Books.objects.get(id=fetchid)
        if(request.method=="GET"):
            book_serializer=BooksSerializer(book)
            return JsonResponse(book_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            book.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            book_serialize=BooksSerializer(book,data=mydata)
            if(book_serialize.is_valid()):
                book_serialize.save()
                return JsonResponse(book_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(book_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    except Books.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)
    
        


@csrf_exempt
def book_list(request):
    if(request.method=="GET"):
        book=Books.objects.all()
        book_serializer=BooksSerializer(book,many=True)
        return JsonResponse(book_serializer.data,safe=False)

@csrf_exempt
def booksPage(request):
    if(request.method=="POST"):
        book_serialize=BooksSerializer(data=request.POST)
        if(book_serialize.is_valid()):
            book_serialize.save()
            return redirect(viewall)
            # return JsonResponse(Books_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)    
      
    else:
        return HttpResponse("No GET method Allowed",status=status.HTTP_404_NOT_FOUND)
