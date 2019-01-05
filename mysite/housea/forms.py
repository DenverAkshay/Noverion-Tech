from django import forms
from .models import Tenant


class TenantCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'c-name'}));
    age = forms.CharField(widget=forms.TextInput(attrs={'id':'c-age','type':'number'}));
    gender = forms.CharField(widget=forms.TextInput(attrs={'id':'c-gender'}));
    mobile_1 = forms.CharField(widget=forms.TextInput(attrs={'id':'c-num1','type':'number'}));
    mobile_2 = forms.CharField(widget=forms.TextInput(attrs={'id':'c-num2','type':'number'}));
    mobile_3 = forms.CharField(widget=forms.TextInput(attrs={'id':'c-num3','type':'number'}));
    address = forms.CharField(widget=forms.Textarea(attrs={'id':'c-address'}));
    city = forms.CharField(widget=forms.TextInput(attrs={'id':'c-city'}));
    country = forms.CharField(widget=forms.TextInput(attrs={'id':'c-country'}));

    class Meta:
        model = Tenant
        fields = ['name','age','gender','mobile_1','mobile_2','mobile_3','address','city','country','location']

class TenantEditForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'e-name'}));
    age = forms.CharField(widget=forms.TextInput(attrs={'id':'e-age','type':'number'}));
    gender = forms.CharField(widget=forms.TextInput(attrs={'id':'e-gender'}));
    mobile_1 = forms.CharField(widget=forms.TextInput(attrs={'id':'e-num1','type':'number'}));
    mobile_2 = forms.CharField(widget=forms.TextInput(attrs={'id':'e-num2','type':'number'}));
    mobile_3 = forms.CharField(widget=forms.TextInput(attrs={'id':'e-num3','type':'number'}));
    address = forms.CharField(widget=forms.Textarea(attrs={'id':'e-address'}));
    city = forms.CharField(widget=forms.TextInput(attrs={'id':'e-city'}));
    country = forms.CharField(widget=forms.TextInput(attrs={'id':'e-country'}));

    class Meta:
        model = Tenant
        fields = ['name','age','gender','mobile_1','mobile_2','mobile_3','address','city','country','location']

class UserLoginForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'id':'u-user','placeholder':'username'}));
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'id':'u-password','placeholder':'password'}))
