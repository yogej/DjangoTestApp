import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf  import csrf_exempt
from django.core import serializers

from employees.models import Employee

# Create your views here.

# create view for getting all employees

def getEmployees(request):
    employees = Employee.objects.all()
    serial=serializers.serialize('json', employees)
    print(serial[3])
    return JsonResponse({'employees':json.loads(serial)})

@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
        member = json.loads(request.body)
        emp=Employee(name=member['name'])
        emp.save()
    return JsonResponse({'employee':member})
