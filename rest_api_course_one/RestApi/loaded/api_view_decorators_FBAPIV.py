from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from RestApi.models import Employee
from RestApi.serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def employee_list(request):
    if request.method == 'GET':
        all_employees = Employee.objects.all()
        all_employees_serializers = EmployeeSerializer(all_employees,many=True)
        return Response(all_employees_serializers.data)

    elif request.method == 'POST':
        employee_data_created = EmployeeSerializer(data = request.data)
        if employee_data_created.is_valid():
            employee_data_created.save()
            return Response(employee_data_created.data,status = status.HTTP_201_CREATED)
        return Response(employee_data_created.errors,status=status.HTTP_502_BAD_GATEWAY)


@api_view(['GET','PUT','DELETE'])
def employee_details(request,pk):
    try:
        single_employee = Employee.objects.get(id=pk)

    except Employee.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        emoloyee_detail = EmployeeSerializer(single_employee)
        return Response(emoloyee_detail.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        employee_data_update = EmployeeSerializer(single_employee,data = request.data)
        if employee_data_update.is_valid():
            employee_data_update.save()
            return Response(employee_data_update.data,status=status.HTTP_202_ACCEPTED)
        return Response(employee_data_update.errors,status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        single_employee.delete()
        all_employees = Employee.objects.all()
        all_employees_serializers = EmployeeSerializer(all_employees,many=True)
        return Response(all_employees_serializers.data,status=status.HTTP_200_OK)

    


