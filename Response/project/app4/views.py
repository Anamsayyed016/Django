from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def app4(request):
    data={'name':'anam','age':27,'quali':'MBA'}
    return JsonResponse(data)