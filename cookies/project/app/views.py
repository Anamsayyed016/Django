from django.shortcuts import render
from datetime import *

# Create your views here.

def set(request):
    data=render(request,'set.html')
    data.set_cookie('name','Anam')  #by de
    data.set_cookie('age','27',max_age=20*60*60)
    data.set_cookie('city','bhopal',httponly=True,secure=True)
    return data