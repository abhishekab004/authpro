from django.shortcuts import render
from tokenapp.models import Employee
from tokenapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    # authentication_classes=[TokenAuthentication,]
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,] 
