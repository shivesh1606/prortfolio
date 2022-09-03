from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home (request):

    obj = Project.objects.all()
    associated_contacts=[]
    obj.order_by('date')
    for project in obj:

        if len(project.associated_contact) != 0:
            associated_contacts.append(project.associated_contact[0])
        
    print(associated_contacts)

    
    context={
        "projects":obj,
        "associated_contacts" : associated_contacts
    }
    
    return render(request,'index.html',context)

def team(request):
    team=Profile.objects.filter(is_current_team_member=True)
    context={
        "team" : team
    }
    return render(request,'dashboard.html',context)


def project_page(request):
    
    obj = Project.objects.all()
    associated_contacts=[]
    obj.order_by('date')
    print(obj)
    context={
        "projects":obj,
    }
    
    return render(request,'index.html',context)
