from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def home (request):
    return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')

def contact(request):
    return render(request,'contact.html')

def team(request):
    return render(request,'team.html')