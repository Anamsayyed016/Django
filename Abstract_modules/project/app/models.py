from django.db import models

# Create your models here.
class Basefield(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    contact=models.IntegerField()

    class Meta:
        abstract=True

class Student(Basefield):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    contact=models.IntegerField()
    course=models.CharField()
    rollno=models.IntegerField()
    fees=models.IntegerField()
    def __str__(self):
        return self.name

class Employee(Basefield):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    contact=models.IntegerField()
    department=models.CharField(max_length=50)
    emp_id=models.EmailField(max_length=50)
    salary=models.IntegerField()

class Client(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    contact=models.IntegerField()
    project=models.CharField(max_length=50)
    billing_status=models=None