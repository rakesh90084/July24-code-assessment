from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def addPage(request):
    if(request.method=="POST"):
        getName=request.POST.get("name")
        getaddress=request.POST.get("address")
        getdepartment=request.POST.get("department")
        getcollege=request.POST.get("college")
        mydict={"name":getName,"address":getaddress,"department":getdepartment,"college":getcollege}
        result=json.dumps(mydict)
        # result=json.dumps(request.POST)
      
        return HttpResponse(result)
    else:
        return HttpResponse("No GET method Allowed")
