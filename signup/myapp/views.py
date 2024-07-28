from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def signup(request):
    context={}
    context['signupForm']=signupForm()
    if request.method=='POST':
        data=signupForm(request.POST)
        if data.is_valid():
            data.save()         
    return render(request,'signup.html',context)