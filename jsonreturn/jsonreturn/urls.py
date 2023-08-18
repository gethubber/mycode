#!/usr/bin/python3

# imports from Django
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('schools/', views.schools),
    path('comics/', views.readparams),  #  comics/?universe=marvel
]

