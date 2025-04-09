from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')

def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')

def register(request):
    print("register page")
    print(request.method)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.META)