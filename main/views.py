from django.shortcuts import render
from.models import *

# Create your views here.
def master(request):
    return render(request,'main/master.html')

def service(request):
    return render(request,'main/service.html')

def contact(request):
    return render(request,'main/contact.html')

def register(request):
    return render(request,'main/register.html')

def careers(request):
    return render(request,'main/careers.html')

def client(request):
    return render(request,'main/client.html')