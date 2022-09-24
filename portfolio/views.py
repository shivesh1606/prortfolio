from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from hitcount.views import HitCountDetailView

from .forms import ContactFormSubmission

# Create your views here.





def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def home (request):

    ip_addr=get_client_ip(request)

    ip_obj=IpModel.objects.filter(ip=ip_addr)
    if len(ip_obj) ==0:
        a=IpModel.objects.create(ip=ip_addr)
        a.save()
    obj = Project.objects.all()
    associated_contacts=[]
    obj.order_by('date')
    for project in obj:

        if len(project.associated_contact.all()) != 0:
            associated_contacts.append(project.associated_contact.all()[0])
        
    print(associated_contacts)

    
    context={
        "count" : IpModel.objects.all().count,
        "projects":obj,

        "associated_contacts" : associated_contacts
    }
    
    return render(request,'index.html',context)

def team(request):
    team=Team.objects.all()
    context={
        "team" : team
    }
    return render(request,'team.html',context)


def publication (request):

    ip_addr=get_client_ip(request)

    ip_obj=IpModel.objects.filter(ip=ip_addr)
    if len(ip_obj) ==0:
        a=IpModel.objects.create(ip=ip_addr)
        a.save()
    obj = Project.objects.all()
    associated_contacts=[]
    obj.order_by('date')
    for project in obj:

        if len(project.associated_contact.all()) != 0:
            associated_contacts.append(project.associated_contact.all()[0])
        
    print(associated_contacts)

    
    context={
        "count" : IpModel.objects.all().count,
        "projects":obj,

        "associated_contacts" : associated_contacts
    }
    
    return render(request,'publication.html',context)


def contact(request):

    if request.method=="POST":
        form = ContactFormSubmission(request.POST)
        if form.is_valid():
            form.save()
            context={
                "msg" : "Form Submitted Successfully"
            }
            
            return render(request,'contact.html',context)
    return render(request,'contact.html')

def equipment(request):

    return render(request,'gallery.html')

def media(request):
    obj=Media.objects.all()
    context={
        "media" : obj
    }
    return render(request,'media.html',context)

def awards(request):
    award=Awards.objects.all()
    context={
        "obj":award
    }
    return render(request,'awards.html',context)


def collaborations(request):

    return render(request,'collaborations.html')


def projects(request):

    return render(request,'projects.html')


def conference(request):

    return render(request,'conference.html')

def invited(request):

    return render(request,'invited.html')

def editorial(request):

    return render(request,'editorial.html')

