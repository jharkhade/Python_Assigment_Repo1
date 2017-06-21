from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
from django import forms

def home(request):
	return render(request, 'myapp/home.html')
def register(request):
	if request.method == 'POST':
		forms = UserRegistrationForm(request.POST)
		if forms.is_valid():
			userObj = forms.cleaned_data
			firstname = userObj['firstname']
			lastname = userObj['lastname']
			username = userObj['username']
			email = userObj['email']
			password = userObj['password']
			if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
				User.objects.create_user(firstname,lastname,username, email, password)
				user = authenticate(username = username, password = password)
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				raise forms.ValidationError ('username or password already exist')
			
	else:
		forms = UserRegistrationForm()
	return render(request, 'myapp/register.html', {'form': forms})