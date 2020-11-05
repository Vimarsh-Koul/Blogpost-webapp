from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from .models import profile

class userregisterationform(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class userupdateform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class profileupdateform(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']            