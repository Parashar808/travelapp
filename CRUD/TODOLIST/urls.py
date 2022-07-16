from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('remove/<int:pk>', views.remove_comp, name='remove_comp'),
    path("contact", views.contact, name="contact"),
    path('create',views.create,name='create'),
    path('update/<str:pk>/',views.update,name='update'),

    #   path('solution', views.solution, name='solution'),
]