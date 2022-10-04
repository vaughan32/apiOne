from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from RestApi.models import Employee
from RestApi.serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class EmployeeViewSet(viewsets.ViewSet):
    def list(self,request):
        employee_list = Employee.objects.all()
        employee_list_serializers = EmployeeSerializer(employee_list,many=True)
        return Response(employee_list_serializers.data,status=status.HTTP_200_OK)

    def create(self,request):
        create_employee = EmployeeSerializer(data = request.data)
        if create_employee.is_valid():
            create_employee.save()
            return Response(create_employee.data, status = status.HTTP_201_CREATED)
        return Response(create_employee.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset,id=pk)
        employee_detatil_serializer = EmployeeSerializer(employee)
        return Response(employee_detatil_serializer.data, status = status.HTTP_200_OK)

    
    def update(self,request,pk=None):
        employee_detailship = Employee.objects.get(id=pk)
        employee_data_update = EmployeeSerializer(employee_detailship,data = request.data)
        if employee_data_update.is_valid():
            employee_data_update.save()
            return Response(employee_data_update.data,status=status.HTTP_202_ACCEPTED)
        return Response(employee_data_update.errors,status = status.HTTP_400_BAD_REQUEST)


    def destroy(self,request,pk):
        employee_detailship = Employee.objects.get(id=pk)
        employee_detailship.delete()
        all_employees = Employee.objects.all()
        all_employees_serializers = EmployeeSerializer(all_employees,many=True)
        return Response(all_employees_serializers.data,status=status.HTTP_200_OK)










