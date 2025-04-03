from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return redirect('/index/')

def index(request):
    return HttpResponse("hello through redirect")