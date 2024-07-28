from django.db import models

# Create your models here.
Is=(('Egg Maggi','Egg Maggi'),('Veg Maggi','Veg Maggi'),('Fry Maggi','Fry Maggi'),('Schezwal Egg Maggi','Schezwal Egg Maggi'),('Schezwal Veg Maggi','Schezwal Veg Maggi'),('Schezwal Fry Maggi','Schezwal Fry Maggi'))
class Billing1(models.Model):
	C_no=models.CharField(max_length=50, default="1" ,null=True)
	S_no=models.CharField(max_length=50)
	Items=models.CharField(max_length=50,choices=Is)
	Quantity=models.CharField(max_length=50)
	PricePerPc=models.CharField(max_length=50)
	Total_Price=models.CharField(max_length=50, null=True)
	pass
	

class Billing2(models.Model):
	C_no=models.CharField(max_length=50, default="1" ,null=True)
	S_no=models.CharField(max_length=50)
	Items=models.CharField(max_length=50,choices=Is)
	Quantity=models.CharField(max_length=50)
	PricePerPc=models.CharField(max_length=50)
	Total_Price=models.CharField(max_length=50, null=True)
	pass