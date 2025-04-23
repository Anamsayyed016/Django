from django.db import models

# Create your models here.
class Basefield(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    contact=models.IntegerField()

class Student(Basefield):
    
    course=models.CharField(max_length=50)
    rollno=models.IntegerField()
    fees=models.IntegerField()
    def __str__(self):
        return self.name

class Employee(Basefield):
    
    department=models.CharField(max_length=50)
    emp_id=models.EmailField(max_length=50)
    salary=models.IntegerField()

class Client(Basefield):
    
    project=models.CharField(max_length=50)
    billing_status=models.CharField(max_length=50)