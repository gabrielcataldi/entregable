from django.contrib import admin
from django.urls import path 
from Family.views import familya

urlpatterns = [  
    path('', familya),
]