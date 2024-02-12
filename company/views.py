from django.shortcuts import render, redirect
from.models import *
from .forms import Student


# Create your views here.
def login(request):
    return render(request,'company/login.html')
def studash(request):
    return render(request,'company/studash.html')
def clidash(request):
    return render(request,'company/clidash.html')
def student(request):
    return render(request,'company/student.html')

def Student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to a success page
    else:
        form = StudentForm()

    return render(request, 'Student.html', {'form': form})
