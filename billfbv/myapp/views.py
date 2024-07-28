from django.shortcuts import render,redirect
from myapp.forms import *
from django.db import transaction
from myapp.models import *

# Create your views here.

def display(request):
	s=Billinga.objects.all()
	d={'stud':s}
	return render(request,'myapp/index.html',d)

def insert_view(request):
	if request.method=="POST":
		a=int(request.POST['S'])	
		b=request.POST['I']
		c=int(request.POST['Q'])
		d=int(request.POST['P'])
		e=int(request.POST['T'])
		f=int(request.POST['C'])
		data=Billinga(S_no=a,Items=b,Quantity=c,PricePerPc=d,Total_Price=e,C_no=f)
		data.save()
		billingb = Billinga(id=request.POST.get('id'),C_no=request.POST.get('C_no'), S_no=request.POST.get('S_no'),Items=request.POST.get('Items'),Quantity=request.POST.get('Quantity'),PricePerPc=request.POST.get('PricePerPc'),Total_Price=request.POST.get('Total_Price'))
		billingb.save()
		Billinga.objects.all().delete()
		return redirect('/')
	return render(request,'myapp/insert.html')

def delete_view(request,id):
	s=Billinga.objects.get(id=id)
	s.delete()
	return redirect('/')


def update_view(request,id):
	s=Billinga.objects.get(id=id)
	if request.method=="POST":
		f=BillingForm(request.POST,instance=s)
		if f.is_valid():
			f.save(commit=True)
		return redirect('/')
	d={'stud':s}
	return render(request,'myapp/update.html',d)

def bill_view(request):
	data=Billinga.objects.all()
	d={'detailes':data}
	return render(request,'myapp/Billing.html',d)