from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request,'home.html',{'value':4})

def home(request):
    return render(request,'home.html',{'value':'django','age':22})