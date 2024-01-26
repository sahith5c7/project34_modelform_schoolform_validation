from django import forms
from app.models import *
from django.core.validators import MinLengthValidator

def validate_for_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('starts with a') 

def validate_for_len(data):
    if len(data)<5:

        raise forms.ValidationError('len is less than 5') 


class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validate_for_a,MinLengthValidator(5)])
    Slocation=forms.CharField(validators=[validate_for_a])
    Sprincipal=forms.CharField()
    email=forms.EmailField()
    Reentermail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)


    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['Reentermail']
        if e!=re:
            raise forms.ValidationError('Invalid data')

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('Ivalid Data')