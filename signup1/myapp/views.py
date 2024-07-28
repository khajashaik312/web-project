from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    context={}
    context['signupForm']=signupForm()
    if request.method=='POST':
        data=signupForm(request.POST)
        if data.is_valid():
            data.save()         
    return render(request,'signup.html',context)

def login(request):
    if request.method=='POST':
        user=request.POST['username']
        pwd=request.POST['password']
        validuser=authenticate(request,username=user,password=pwd)
        if validuser is not None:
            if request.user.is_authenticated:
                return render(request,'home.html')
            else:
                login(request,validuser)
                return render(request,'home.html')
        else:
            return HttpResponse('Invalid User')
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('loginpage')

def home(request):
    return render(request,'home.html')