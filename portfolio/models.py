from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from datetime import timedelta
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

categotry = {
    ('Journal','Journal'),
    ('Book Chapters','Book Chapters'),
    ('Books','Books'),
    ('International Reports','International Reports'),
    ('Conference','Conference'),
    

}
categotry_team_member = {
    ('Team','Team'),
('Alumini','Alumini')

}

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=250, null=True,blank=True)
    photo = models.FileField(null=True, blank=True)
    category = models.CharField(max_length=60, choices=categotry_team_member ,default='Team')
    def __str__(self):
        return self.name
    
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    info =models.TextField()
    category = models.CharField(max_length=60, choices=categotry ,default='Journal')

    date = models.DateField(null=True)

    def __str__(self):
        return self.category +" - "+self.info
    

class View_count(models.Model):
    count=models.IntegerField(default=0)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')

class IpModel(models.Model):
    ip=models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class Contact_form(models.Model):
    name=models.CharField(max_length=250, null=True,blank=True)
    email=models.EmailField(max_length=3000)
    subject=models.CharField(max_length=3000)
    affilation=models.CharField(max_length=3000)
    message=models.TextField()

    def __str__(self):
        return self.name + " - " + self.email

class Awards(models.Model):
    image=models.FileField(null=True, blank=True)
    title=models.CharField(max_length=3000,null=True, blank=True)
    url=models.CharField(max_length=3000,null=True, blank=True)
    def __str__(self):
        return self.title
    