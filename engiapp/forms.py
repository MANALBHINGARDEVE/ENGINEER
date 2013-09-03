from django import forms 
import re
from django.contrib.auth.models import User 
from django.forms.extras.widgets import SelectDateWidget
BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')

class RegistrationForm(forms.Form): 
    first_name=forms.CharField(label=u'First Name')
    last_name=forms.CharField(label=u'Last Name')
    email = forms.EmailField(label=u'Email') 
    password1 = forms.CharField(label=u'Password',widget=forms.PasswordInput() ) 
    password2 = forms.CharField(label=u'Confirm Password', widget=forms.PasswordInput()) 
    date_of_birth=forms.DateField(label=u'Date of Birth',widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    country=forms.CharField(label=u'Country', max_length=50) 
    state=forms.CharField(label=u'State', max_length=50) 
    city=forms.CharField(label=u'City', max_length=50) 
    address=forms.CharField(label=u'Address', max_length=30) 
    institution_name=forms.CharField(label=u'School Name', max_length=50) 
    def clean_password2(self):
        if 'password1' in self.cleaned_data: 
            password1 = self.cleaned_data['password1'] 
            password2 = self.cleaned_data['password2'] 
            if password1 == password2:
                return password2 
        raise forms.ValidationError('Passwords do not match.') 
    def clean_email(self):
	email=self.cleaned_data['email']
	try:
		User.objects.get(email=email)
	except User.DoesNotExist:
		return email
	raise forms.ValidationError('An account is already registerd under this email.')
