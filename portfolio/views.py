from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from hitcount.views import HitCountDetailView

from .forms import ContactFormSubmission
import json

from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.





def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    ip=ip.split(":")
    ip=ip[0]
    print(ip)
    return ip

def home (request):

    ip_addr=get_client_ip(request)

    ip_obj=IpModel.objects.filter(ip=ip_addr)
    if len(ip_obj) ==0:
        a=IpModel.objects.create(ip=ip_addr)
        a.save()
    # obj = Publication.objects.all()
    # associated_contacts=[]
    # obj.order_by('date')
    # for Publication in obj:

    #     if len(Publication.associated_contact.all()) != 0:
    #         associated_contacts.append(Publication.associated_contact.all()[0])
        
    # print(associated_contacts)

    
    context={
        "count" : IpModel.objects.all().count,
        # "Publications":obj,

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
    obj = Publication.objects.all()
    obj.order_by('date')
    
    context={
        "count" : IpModel.objects.all().count,
        "projects":obj,
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
    award=Award.objects.all()
    context={
        "obj":award
    }
    return render(request,'awards.html',context)


def collaborations(request):
    obj=Collaboration.objects.values()

 
    # data_json = json.dumps(list(obj), cls=DjangoJSONEncoder)



    # data =list(obj)
    # print(data)
    # new_data=[]
    # for d in data:
    #     l=[]
    #     l.append(d["title"])
    #     dict_ob={}
    #     dict_ob["lat"]=float(d["lat"])
    #     dict_ob["lng"]=float(d["lng"])
    #     l.append(dict_ob)
    #     new_data.append(l)
    # print(new_data)
    # context={
    #     "obj":data,
    #     "django_list":new_data
    # }
    obj=Collaboration.objects.all()
    context={
        "obj":obj
    }
    # print(JsonResponse(data,safe = False).status)
    return render(request,'collaborations.html',context)


def projects(request):
    obj = Project.objects.all()
    obj.order_by('date')
    
    context={
        "count" : IpModel.objects.all().count,
        "projects":obj,
    }
    
    return render(request,'projects.html',context)


def conference(request):
    obj = Reasearch.objects.filter(category='Conference Presentation')
    obj.order_by('date')
    
    context={
        "count" : IpModel.objects.all().count,
        "projects":obj,
    }
    print(obj)
    return render(request,'conference.html',context)

def invited(request):
    obj = Reasearch.objects.filter(category='Invited Talks')
    obj.order_by('date')
    
    context={
        "count" : IpModel.objects.all().count,
        "projects":obj,
    }
    print(obj)

    return render(request,'invited.html',context)

def editorial(request):
    obj = Reasearch.objects.filter(category='Editorial Boards')
    obj.order_by('date')
    
    context={
        "count" : IpModel.objects.all().count,
        "projects":obj,
    }
    return render(request,'editorial.html',context)



def gallery(request):
    obj = Gallery_Image.objects.all()
    
    context={
        "projects":obj,
    }
    return render(request,'gallery_image.html',context)

