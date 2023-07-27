from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def homePage(request):
    return render(request,"userapp/home.html")

def signupPage(request):
    
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('pass2')
        
        if password1!=password2:
         return HttpResponse("Password doesn't match. Please try again!")
        
        else:
            my_user=User.objects.create_user(uname,email,password1)   
            my_user.save()
            return redirect ('login')
    
    return render(request,"userapp/signup.html")

def loginPage(request):
    
    if request.method=='POST':
        uname=request.POST.get('username')
        password=request.POST.get('pass1')
        user=authenticate(request,username=uname,pass1=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password are Incorrect")
          
    return render(request,"userapp/login.html")

def logoutPage(request):
         
    logout (request)
    
    return redirect ('login')

