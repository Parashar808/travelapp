from django.urls import path

from accounts.views import information
from . import views

urlpatterns=[
    

    path('',views.index, name='index'),
    path('information/',views.information,name='information')
    
]