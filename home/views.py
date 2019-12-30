from django.shortcuts import render

def index(request):
	return render(request, 'home/homepage.html')

def contact(request):
	return render(request, 'home/contact.html') #{'content:',['<h2>Office hours: 11:30AM-9:00PM Mon-Fri</h2>','<b>Contact</b>: diazj1941@gmail.com','<b>Jeremy Diaz</b>, Editor In-Chief.']})

def about(request):
	return render(request, 'home/about.html')
def brightCtrl(request):
	return render(request, 'about/brightCtrl.html')
# Create your views here.
