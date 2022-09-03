from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from datetime import timedelta

categotry = {
    ('Journal','Journal'),
    ('Articles','Articles'),
    ('International Reports','International Reports')

}

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=250, null=True,blank=True)
    country=models.CharField(max_length=250, null=True,blank=True)
    university= models.CharField(max_length=250, null=True,blank=True)
    is_current_team_member=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    info =models.TextField()
    category = models.CharField(max_length=60, choices=categotry ,default='Journal')
    associated_contact=models.ManyToManyField(
        Profile, related_name='users', blank=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.category +" - "+self.info
    
