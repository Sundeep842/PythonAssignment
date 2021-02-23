from django.urls import path
from . import views


urlpatterns=[
    path('',views.EmployeeHome),
    path('api/manager',views.ManagerHome),
    path('api/employee',views.EmployeeHome)

]