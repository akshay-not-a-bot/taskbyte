from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def landing(request):
    return HttpResponse("This is the landing page for Account page!!!")
