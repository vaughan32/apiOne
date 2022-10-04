from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from RestApi.models import Employee
from RestApi.serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def employee_list(request):
    if request.method == 'GET':
        all_employees = Employee.objects.all()
        all_employees_serializers = EmployeeSerializer(all_employees,many=True)
        return JsonResponse(all_employees_serializers.data,safe=False,status=200)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_data_created = EmployeeSerializer(data = employee_data)
        if employee_data_created.is_valid():
            employee_data_created.save()
            return JsonResponse(employee_data_created.data,status = 201)
        return JsonResponse(employee_data_created.errors,status = 400)


@csrf_exempt
def employee_details(request,pk):
    try:
        single_employee = Employee.objects.get(id=pk)

    except Employee.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        emoloyee_detail = EmployeeSerializer(single_employee)
        return JsonResponse(emoloyee_detail.data,status=200)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee_data_update = EmployeeSerializer(single_employee,data = employee_data)
        if employee_data_update.is_valid():
            employee_data_update.save()
            return JsonResponse(employee_data_update.data,status=201)
        return JsonResponse(employee_data_update.errors,status = 400)

    elif request.method == 'DELETE':
        single_employee.delete()
        all_employees = Employee.objects.all()
        all_employees_serializers = EmployeeSerializer(all_employees,many=True)
        return JsonResponse(all_employees_serializers.data,safe=False,status=200)

    

