from django.contrib.auth.forms import forms
from .models import Product
from . models import User
from . models import BookForm

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','propertytransaction']
        labels= {
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email',
            'propertytransaction':'Property Transaction'
        }

    widgets={
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'propertytransaction':forms.TextInput(attrs={'class':'form-control'})
    }   


class BookForm(forms.ModelForm):
    class Meta:
        model=BookForm
        fields='__all__'

