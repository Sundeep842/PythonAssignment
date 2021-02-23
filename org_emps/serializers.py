from rest_framework import serializers  
from .models import Employee,Manager

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class Managerserializer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        fields='__all__'

        