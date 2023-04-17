from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('viewproperty/',views.viewproperty,name='viewpro'),
    path('add/',views.add_user,name='add_user'),
    path('advertise/',views.advertise,name='advertise'),
    path('book/',views.booking,name='book'),
    path('productcreate/',views.productcreate,name='productcreate'),
   
]