from django.db import models

# Create your models here.

#id is primary key which is automatically generated for Employee model
#manager is foreign key for id of employee table

class Manager(models.Model):
    id=models.IntegerField(primary_key=True)
class Employee(models.Model):
    name = models.CharField(max_length=30)
    manager = models.ForeignKey(Manager,null=True, on_delete=models.CASCADE)

