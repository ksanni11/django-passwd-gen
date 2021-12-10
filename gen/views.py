from django.shortcuts import render
from django.http import HttpResponse
import random

# Home view
def home(request): 
	return render(request, 'gen/home.html')

# Password View
def password(request):
	
	characters = list('abcdefghijklmnopqrstuvwxyz')
	length = int(request.GET.get('length', 10))
	
	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*()'))

	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))

	passwd = ''
	for x in range(length):
		passwd += random.choice(characters)

	return render(request, 'gen/password.html', {'password':passwd})

#About View
def about(request):
	return render(request, 'gen/about.html')