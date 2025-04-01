from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
# Create your views here.

def home(request):
    return render (request,'home.html')

def index (request):
    return redirect('https://www.google.com/')

def tc (request):
    return HttpResponse("<h1> hello <h1>")

def js (request):
    data={'name':True,'age':False,'quali':None}
    return JsonResponse(data)
    
