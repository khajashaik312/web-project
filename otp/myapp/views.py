from django.shortcuts import render,redirect
from django.http import HttpResponse


                                            # Sending an OTP to a mail

import os
import math
import random
import smtplib

def otp(request):
    digits="0123456789abcdefghijklmnopqrstuvwxyz"
    OTP=""
    length=len(digits)
    for i in range(6):
        OTP+=digits[math.floor(random.random()*length)]
    otp = OTP + " is your OTP"
    msg= otp
    if request.method=='POST':
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("khajashaik312@gmail.com", "fbxoqneawylhwvsh")
        emailid = request.POST['email']
        s.sendmail('&&&&&&&&&&&',emailid,msg)
        return render (request,'gototp.html')
    return render (request,'getotp.html')

def otpVerify(request):
    if request.method=="POST":
        profile=Profile.objects.get()     
        if request.COOKIES.get('can_otp_enter')!=None:
            if(profile.otp==request.POST['otp']):
                red=redirect("home")
                red.set_cookie('verified',True)
                return red
            return HttpResponse("wrong otp")
        return HttpResponse("10 minutes passed")        
    return render(request,"otp.html")