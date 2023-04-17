from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User,auth
from .models import Product
from .models import Propertydata
from .models import BookForm
from .forms import *
# Create your views here.




def home(request):
    return render(request,'property/home.html')



def add_user(request):
    if request.method =='POST':
        form =UserForm(request.POST)
        if form.is_valid():
            new_first_name =form.cleaned_data['first_name']
            new_last_name =form.cleaned_data['last_name']
            new_email =form.cleaned_data['email']
            new_propertytransaction =form.cleaned_data['propertytransaction']

        new_user = User(
            first_name=new_first_name,
            last_name =new_last_name,
            email=new_email,
            propertytransaction=new_propertytransaction

        )
        new_user.save()
        return render(request,'property/adduser.html',{
            'form':UserForm(),
            'success':True
        })
    
    else:
        form=UserForm()
        return render(request,'property/adduser.html',{
            'form':UserForm()
        })



def viewproperty(request):
    dests=Product.objects.all()
    return render(request,'property/viewpro.html',{'dests':dests})


def advertise(request):
    propertydata=Propertydata.objects.all
    context={
        'propertydata':propertydata
    }
    return render(request,'property/advertisement.html',context)

    

def productcreate(request):
    form = ProductForm(request.POST or None,request.FILES or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return render(request,'property/addimage.html')
    return render(request,'property/form_template.html',{'form':form})

def booking(request):
    form = BookForm(request.POST or None,request.FILES or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return render(request,'property/fav.html')
    return render(request,'property/booking.html',{'form':form})


