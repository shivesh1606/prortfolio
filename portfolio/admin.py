from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse
from .models import *


admin.site.register(Team)
admin.site.register(Publication)
admin.site.register(View_count)
admin.site.register(IpModel)
admin.site.register(Contact_form)
admin.site.register(Award)
admin.site.register(Media)
admin.site.register(Project)
admin.site.register(Reasearch)
admin.site.register(Map_Location)
admin.site.register(Gallery_Image)
admin.site.register(Collaboration)
