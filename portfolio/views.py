from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
  return render(request, 'portfolio/home.html')

def about(request):
  return render(request, 'portfolio/about.html')

def services(request):
  return render(request, 'portfolio/services.html')

def skills(request):
  return render(request, 'portfolio/skills.html')

def contact(request):
  return render(request, 'portfolio/contact.html')