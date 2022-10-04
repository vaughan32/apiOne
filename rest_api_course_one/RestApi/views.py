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

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
  













































class EmployeeList(APIView):
    def get(self,request):
        all_employees = Employee.objects.all()
        all_employees_serializers = EmployeeSerializer(all_employees,many=True)
        return Response(all_employees_serializers.data,status = status.HTTP_200_OK)

    def post(self,request):
        create_employee = EmployeeSerializer(data=request.data)
        if create_employee.is_valid():
            create_employee.save()
            return Response(create_employee.data,status = status.HTTP_201_CREATED)
        return Response(create_employee.errors,status=status.HTTP_502_BAD_GATEWAY)




class EmployeeDetail(APIView):
    def get_object(self,pk):
        try:
            return Employee.objects.get(id=pk)
        
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        
    def get(self,request,pk):
        employee_detailship = self.get_object(pk)
        detail_employee = EmployeeSerializer(employee_detailship)
        return Response(detail_employee.data,status=status.HTTP_200_OK)
        


    def put(self,request,pk):
        employee_detailship = self.get_object(pk)
        employee_data_update = EmployeeSerializer(employee_detailship,data = request.data)
        if employee_data_update.is_valid():
            employee_data_update.save()
            return Response(employee_data_update.data,status=status.HTTP_202_ACCEPTED)
        return Response(employee_data_update.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        employee_detailship = self.get_object(pk)
        employee_detailship.delete()
        all_employees = Employee.objects.all()
        all_employees_serializers = EmployeeSerializer(all_employees,many=True)
        return Response(all_employees_serializers.data,status=status.HTTP_200_OK)

