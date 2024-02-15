from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from .form import SignUpForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_view(request):
    form = SignUpForm()
    print(form)
    return render(request,'registration/signup.html',{'form':form})

def home_view(request):
    return render(request, 'home/home.html')


def login_view(request):
    pass