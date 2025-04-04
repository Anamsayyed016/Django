from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
# Create your views here.

def home(request):

    data={'name':'anam','age':27,'quali':'MBA'}
    # data=[{'name':'Anam','age':27},{'name':'Ali','age':25}]
    user={'name':'Roy','city':'Bhopal'}

    # return render(request,'home.html',data)
    # return render(request,'home.html',{'key1':data})
    return render(request,'cart.html',{'key1':user,'key2':data})


def index (request):
    return redirect('https://www.google.com/')

def tc (request):
    return HttpResponse("<h1> hello <h1>")

def js (request):
    data={'name':True,'age':False,'quali':None}
    return JsonResponse(data)
    
