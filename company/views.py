from django.shortcuts import render, redirect
from.models import *



# Create your views here.
def login(request):
    return render(request,'company/login.html')
def studash(request):
    return render(request,'company/studash.html')
def clidash(request):
    return render(request,'company/clidash.html')
def student(request):
    return render(request,'company/student.html')

