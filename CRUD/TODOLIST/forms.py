from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Complain

# Create your forms here.

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)


class ComplainForm(ModelForm):
	class Meta:
		model=Complain
		fields = '__all__'

