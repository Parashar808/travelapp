from django.urls import path

# from accounts.views import information
from . import views

urlpatterns=[
    

    path('',views.index, name='index'),
    path('information/',views.information,name='information'),
    path('information/payment',views.payment,name='payment'),
    path('information/information/payment/paid',views.paid,name='paid')


    
]