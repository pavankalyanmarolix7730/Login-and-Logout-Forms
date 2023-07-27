from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'signin/index.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()        

        messages.success(request,'Your Account has been Created Successfully.')
        return redirect('login')
    
    return render(request, 'signin/signup.html')

def login(request):
    return render(request, 'signin/login.html')

def logout(request):
    return render(request, 'signin/logout.html')
