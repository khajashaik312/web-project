from django.shortcuts import render,redirect
from django.db import connection
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
		id_to_delete = request.POST.get('id_to_delete')
		with connection.cursor() as cursor:
			cursor.execute("DELETE FROM khaja.myapp_billing1 WHERE id = %s", [id_to_delete])
		a=request.POST['S']	
		b=request.POST['I']
		c=int(request.POST['Q'])
		d=int(request.POST['P'])
		e=int(request.POST['T'])
		data=Billing1(S_no=a,Items=b,Quantity=c,PricePerPc=d,Total_Price=e)
		data.save()
		billing_history = BillingHistory(S_no=a, Items=b, Quantity=c, PricePerPc=d, Total_Price=e)
		billing_history.save()
		print("Record saved successfully!")
		return redirect('/')
	else:
	    return render(request,'myapp/insert.html')	

def delete_view(request, S_no):
    Billing1.objects.filter(S_no=S_no).delete()
    print("Record deleted successfully!")
    return redirect('/')

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