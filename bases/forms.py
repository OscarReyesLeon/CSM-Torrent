from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import models
from django.forms import fields
from django import forms
from django.forms.widgets import PasswordInput

from .models import User

class UserCreationForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(UserCreationForm,self).__init__(*args,**kwargs)

    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(UserChangeForm):
    def __init__(self,*args,**kwargs):
        super(UserChangeForm,self).__init__(*args,**kwargs)

    class Meta:
        model = User
        fields = '__all__'

class Userform(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password']
        widget = {'email': forms.EmailInput,
                   'password': forms.PasswordInput }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })