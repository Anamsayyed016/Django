from django.shortcuts import render
from.models import *
# Create your views here.

def aadhar1(request):
    data=Aadhar.objects.all()
    print(data.values())
    # print(data.values_list())

    data=Aadhar.objects.get(aadhar=125466622)
    print(data.aadhar)
    print(data.create_date)
    print(data.created_by)
    x=data.xyz   #for reverse accesing
    print(x.stu_name)
    print(x.stu_email)
    print(x.stu_contant)

def student1(request):
    data=Student.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())

    data=Student.objects.get(stu_name='anam')
    print(data.stu_name)
    print(data.stu_email)
    print(data.aadhar_no)
    x=data.aadhar_no  #for forward accessing

    print(x.aadhar)
    print(x.create_date)
    print(x.created_by)