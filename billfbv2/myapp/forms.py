from django import forms
from myapp.models import *
class BillingForm(forms.ModelForm):
	class Meta:
		model=Billing1
		fields='__all__'