from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as A_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout as A_logout

from customer.forms import SignUpForm , FeedBackForm
from django.http import HttpResponse

@login_required
def home(request):
    return render(request,'customer/home.html')

def signup(request):
    if request.method == 'POST':
        form  = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            #user.save()
            messages.success(request, "Registration successful." )
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = SignUpForm()
    return render(request,'customer/signup.html',{'form':form})

def login(request):
    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                A_login(request,user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="customer/login.html", context={"login_form":form})

@login_required
def feedback(request):
    if request.method=="POST":
        data=FeedBackForm(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request, "FeedBack Submitted successfully." )
            return redirect("home")            
    form=FeedBackForm()
    return render(request,template_name="customer/feedback.html",context={'form':form})

def logout(request):
    A_logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("login")