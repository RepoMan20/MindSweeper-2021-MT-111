from django import forms  
from home.models import *
class Patient_register(forms.Form):
    Email_id = forms.EmailField(max_length = 200, label="Email Id" )
    Passowrd = forms.CharField(widget=forms.PasswordInput, label="Password")

