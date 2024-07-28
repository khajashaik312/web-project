from django import forms
from myapp.models import *
class BillingForm(forms.ModelForm):
	class Meta:
		model=Billinga
		fields='__all__'

class BillingForm(forms.ModelForm):
	class Meta:
		model=Billingb
		fields='__all__'