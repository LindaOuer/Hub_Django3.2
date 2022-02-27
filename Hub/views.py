from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function based views
def homePage(request):
    return HttpResponse('<h1>Welcome To ... </h1>')