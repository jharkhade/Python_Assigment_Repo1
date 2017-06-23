from django import forms

class UserRegistrationForm(forms.Form):
	firstname = forms.CharField(
		required=True,
		label='firstname',
		max_length=32
	)
	lastname = forms.CharField(
		required=True,
		label='lastname',
		max_length=32
	)
	
	username = forms.CharField(
			required = True,
			label = 'Username',
			max_length = 32
		)
	email = forms.CharField(
			required = True,
			label = 'Email',
			max_length = 32,
		)
	password = forms.CharField(
			required = True,
			label = 'Password',
			max_length = 32,
			widget = forms.PasswordInput()
		)