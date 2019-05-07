#USer forms has functions for user password inputs
# wish use of djanog insert imports with auth for users
# Required models for user = username , email, and password

from django.contrib.auth.models import User
from django import forms

#User input function for password here 
class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
	
        model = User
        fields = ['username', 'email', 'password']


			




		
		


