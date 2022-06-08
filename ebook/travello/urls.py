from django.urls import path

# from accounts.views import information
from . import views

urlpatterns=[
    

    path('',views.index, name='index'),
    path('information',views.information,name='information'),
    path('payment',views.payment,name='payment'),
    path('paid',views.paid,name='paid'),
    path('payform',views.payform,name='payform')
    


    
]