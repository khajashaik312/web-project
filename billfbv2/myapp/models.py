from django.db import models

# Create your models here.
Is=(('Egg Maggi','Egg Maggi'),('Veg Maggi','Veg Maggi'),('Fry Maggi','Fry Maggi'),('Schezwal Egg Maggi','Schezwal Egg Maggi'),('Schezwal Veg Maggi','Schezwal Veg Maggi'),('Schezwal Fry Maggi','Schezwal Fry Maggi'))
class Billing1(models.Model):
	S_no=models.CharField(max_length=50)
	Items=models.CharField(max_length=50,choices=Is)
	Quantity=models.CharField(max_length=50)
	PricePerPc=models.CharField(max_length=50)
	Total_Price=models.CharField(max_length=50)

class BillingHistory(models.Model):
    S_no = models.CharField(max_length=50)
    Items = models.CharField(max_length=50, choices=Is)
    Quantity = models.CharField(max_length=50)
    PricePerPc = models.CharField(max_length=50)
    Total_Price = models.CharField(max_length=50)