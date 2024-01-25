from django import forms
from a_panel.models import * 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    icon = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Category
        fields = ['name','icon']
        
class SubcategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Subcategory
        fields = ['name','category']

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    desc = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price_new = forms.DecimalField(max_digits=5,decimal_places=2,widget=forms.NumberInput(attrs={'class':'form-control'}),required=False)
    price_old = forms.DecimalField(max_digits=5,decimal_places=2,widget=forms.NumberInput(attrs={'class':'form-control'}))
    image = forms.ImageField()
    subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Product
        fields = ['name','price_new','price_old','image','subcategory']


class UserCreateForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','password1','password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))

class WorkerForm(forms.ModelForm):

    rol = (
        (1,'Owner'),
        (2,'Administration'),
        (3,'Manager'),
    )

    user = forms.ModelChoiceField(queryset=User.objects.filter(is_superuser=True),widget=forms.Select(attrs={'class':'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'First name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Last name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Phone number','value':'+993'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Address'}))
    age = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    image = models.ImageField()
    role = forms.CharField(widget=forms.Select(choices=rol,attrs={'class':'form-control'}))

    class Meta:
        model = Worker
        fields = ['user','name','surname','email','phone','address','age','image','role']
