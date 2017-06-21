from django import forms
class UserRegistrationForm(forms.Form):
	firstname = forms.CharField(
		required=True,
		label='Firstname',
		max_length='40'
	)
	
	lastname = forms.CharField(
		required=True,
		label='Lastname',
		max_length='40'
	)
	username = forms.CharField(
		required=True,
		label='Username',
		max_length=32
	)
	email = forms.CharField(
		required=True,
		label='Email',
		max_length=32,
	)
	password = forms.CharField(
		required=True,
		label='Password',
		max_length=32,
		widget=forms.PasswordInput()
	)