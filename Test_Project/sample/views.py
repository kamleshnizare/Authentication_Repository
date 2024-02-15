from django.shortcuts import render
from .form import SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.

def signup_view(r):
    if r.method == 'POST':
        form = SignUpForm(r.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/home')
    else:
        form = SignUpForm()
        return render(r, 'registration/signup.html', {'form': form})

@login_required
def login_view(r):
    if r.method == 'POST':
        username = r.POST['username']
        password = r.POST['password']
        user = auth.authenticate(username = username , password = password)
        if user is not None:
            auth.login(r,user)
            return HttpResponseRedirect('registration/signup.html')
    else:
        return render(r,'registration/login.html')



def home_view(r):
    return render(r,'registration/home.html')
