#!/usr/bin/python3

# imports from Django
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('ierror/', views.ierror),
    path('success/', views.success),
]

# add this snippet to the bottom of ~/boxstore/boxstore/urls.py
urlpatterns += [
    path('header/', views.customheader),   # call our custom header
    path('created/', views.customcode),       # call our 201 response code
]

