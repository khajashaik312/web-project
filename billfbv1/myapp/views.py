from django.shortcuts import render,redirect
from myapp.forms import *
from django.db import transaction
from myapp.models import *

# Create your views here.

def display(request):
	s=Billing1.objects.all()
	d={'stud':s}
	return render(request,'myapp/index.html',d)

def insert_view(request):
	if request.method=="POST":
		a=request.POST['S']	
		b=request.POST['I']
		c=int(request.POST['Q'])
		d=int(request.POST['P'])
		e=int(request.POST['T'])
		f=int(request.POST['C'])
		data=Billing1(S_no=a,Items=b,Quantity=c,PricePerPc=d,Total_Price=e,C_no=f)
		data.save()
		data=Billing2(S_no=a,Items=b,Quantity=c,PricePerPc=d,Total_Price=e,C_no=f)
		data.save()
		return redirect('/')
	return render(request,'myapp/insert.html')

def delete_view(request,id):
	s=Billing1.objects.get(id=id)
	s.delete()
	return redirect('/')


def update_view(request,id):
	s=Billing1.objects.get(id=id)
	if request.method=="POST":
		f=BillingForm(request.POST,instance=s)
		if f.is_valid():
			f.save(commit=True)
		return redirect('/')
	d={'stud':s}
	return render(request,'myapp/update.html',d)

def bill_view(request):
	data=Billing1.objects.all()
	d={'detailes':data}
	return render(request,'myapp/Billing.html',d)
