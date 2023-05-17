from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import AdmissionForm
from schoolapp.models import Registration,AdmissionPage


def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            filter_name = Registration.objects.filter(username=username).exists()
            if filter_name:
                messages.info(request, 'UserName already exists')
                return redirect("register")
            else:
                task = Registration(username=username, password=password, cpassword=cpassword)
                task.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            # return redirect('home')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user_data = Registration.objects.filter(username=username, password=password)
        if user_data:
            return redirect("new")
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    return render(request, 'login.html')


def new(request):
    return render(request, 'new.html')


def form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        dob = request.POST.get('dob', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        mob = request.POST.get('mob', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        department = request.POST.get('department', '')
        courses = request.POST.get('courses', '')
        purposes = request.POST.get('purposes', '')
        materials = request.POST.get('materials', '')
        form_list = AdmissionPage(name=name, dob=dob, age=age, gender=gender, mob=mob, email=email, address=address,
                             department=department, courses=courses, purposes=purposes, materials=materials)
        form_list.save()
        return redirect("success")

    return render(request, 'newpage.html')


def success(request):
    messages.success(request, "Admission Confirmed")
    return render(request, 'message.html')

# Create your views here.
