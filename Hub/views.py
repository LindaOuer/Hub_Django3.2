from django.shortcuts import render
from django.http import HttpResponse


from .models import Student

# Create your views here.
# function based views


def homePage(request):
    return HttpResponse('<h1>Welcome To ... </h1>')


def list_Students(request):
    list = Student.objects.all()
    return render(
        request,
        'Hub/list_students.html',
        {
            'students': list,
        },
    )
