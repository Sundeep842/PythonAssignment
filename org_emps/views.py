from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from .models import Manager,Employee
from rest_framework.views import APIView
from .serializers import Employeeserializer,Managerserializer
from rest_framework.parsers import JSONParser
from .sql import  Employeequery,Managerquery

@csrf_exempt
def EmployeeHome(request):
    if(request.method=="GET"):
        emp  = Employeequery
        serializer= Employeeserializer(emp, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif(request.method=="POST"):
          data=JSONParser().parse(request)
          serializer=Employeeserializer(data=data)
          if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,safe=False)
          return JsonResponse(serializer.errors,status=400)

def ManagerHome(request):
    if(request.method=="GET"):
        emp  = Managerquery
        serializer= Managerserializer(emp, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif(request.method=="POST"):
          data=JSONParser().parse(request)
          serializer=Managerserializer(data=data)
          if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,safe=False)
          return JsonResponse(serializer.errors,status=400)
        

