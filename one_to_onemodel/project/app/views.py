from django.shortcuts import render
from.models import *
# Create your views here.

def aadhar(request):
    data=Aadhar.objects.all()
    print(data.values())
    # print(data.values_list())