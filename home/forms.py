from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from home.models import *
from a_panel.models import Customer

class RegisterForm(UserCreationForm):
    username = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'txt-input',"name":'username'}))
    email = forms.CharField(required=False,widget=forms.EmailInput(attrs={'class':'txt-input','name':'email'}))
    password1 = forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class':'txt-input','name':'password1'}))
    password2 = forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class':'txt-input','name':'password2'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'txt-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'txt-input'}))
    
class OrderForm(forms.ModelForm):

    p = [
        ('PASH','PASH'),
        ('Credit','Credit'),
    ]

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','border':' 1px solid black','style':"width:85%;"}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':"width:85%;"}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':"width:85%;"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',"placeholder":'+993','style':"width:85%;"}))
    payment_type = forms.CharField(widget=forms.RadioSelect(attrs={'class':'txt-input'},choices=p))
    note = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',"rows":"4"}))

    class Meta:
        model = Order
        fields = ['name','surname','address','phone_number','payment_type','note']


class CustomerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'txt-input',"placeholder":'Your name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'txt-input',"placeholder":'Email Address'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'txt-input',"placeholder":'Phone Number'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'txt-input','cols':'30','row':'9',"placeholder":'Leave Message'}))

    class Meta:
        model = Customer
        fields = ['name','email','phone','message']
