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
admin.site.register(Awards)
admin.site.register(Media)
