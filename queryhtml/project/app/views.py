from django.shortcuts import render
from .models import Students
# Create your views here.

def landing(request):
    return render(request,'landing.html')

def first5(request):
    data=Students.objects.all()[0:6]
    return render(request,'table.html',{'data':data})

def last5(request):
    data=Students.objects.all().order_by('-stu_name')[:5]
    return render(request,'table.html',{'data':data})

def allstu(request):
    data = Students.objects.all
    return render(request,'table.html',{'data':data})

def assen(request):
    data = Students.objects.all()[0:11]
    return render(request,'table.html',{'data':data})

def dssend(request):
    data = Students.objects.all().order_by('-stu_sno',)[0:11]
    return render(request,'table.html',{'data':data})

