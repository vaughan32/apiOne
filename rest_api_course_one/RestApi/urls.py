from django.urls import path,include
from . import views
from RestApi.views import EmployeeViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('employees',EmployeeViewSet,basename='employee')

urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
]
