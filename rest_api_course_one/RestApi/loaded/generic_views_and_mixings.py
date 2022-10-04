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


class GenricApiView(generics.GenericAPIView,mixins.ListModelMixin,
mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin

):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_field = 'pk'

    def get(self,request,pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,pk=None):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)










