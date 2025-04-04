from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    name,city='anam','bhopal'

    # return redirect(f'/index/?name={name}&city={city}')
    return redirect('/index/?name={}&city={}.format(name,city)')

def index(request):
    print(request.method)
    print(request.GET)
    x=request.GET.get('name')
    y=request.GET.get('city')
    print(x,y)
    # return HttpResponse("hello through redirect")