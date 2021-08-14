from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def addPage(request):
    if(request.method=="POST"):
        getName=request.POST.get("name")
        getadmno=request.POST.get("admno")
        getrollno=request.POST.get("rollno")
        getcollege=request.POST.get("college")
        getparentname=request.POST.get("parentname")
        mydict={"name":getName,"admno":getadmno,"rollno":getrollno,"college":getcollege,"parentname":getparentname}
        result=json.dumps(mydict)
        # result=json.dumps(request.POST)
      
        return HttpResponse(result)
    else:
        return HttpResponse("No GET method Allowed")
