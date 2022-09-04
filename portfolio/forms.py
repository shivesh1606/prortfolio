from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *


class ContactFormSubmission(forms.ModelForm):

    class Meta:
        model = Contact_form
        fields = '__all__'

