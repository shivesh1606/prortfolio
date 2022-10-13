"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'server'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home_page"),
    path('team/',views.team,name="team_page"),
    path('publication/',views.publication,name="publication_page"),
    path('contact/',views.contact,name="contact_page"),
    path('equipment/',views.equipment,name="equipment_page"),
    path('media/',views.media,name="media_page"),
    path('awards/',views.awards,name="awards_page"),
    path('collaborations/',views.collaborations,name="collaborations_page"),
    path('projects/',views.projects,name="projects_page"),
    path('conference/',views.conference,name="conference_page"),
    path('invited/',views.invited,name="invited_page"),
    path('editorial/',views.editorial,name="editorial_page"),
    path('gallery/',views.gallery,name="gallery_page")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
