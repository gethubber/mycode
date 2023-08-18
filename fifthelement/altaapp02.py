#!/usr/bin/python3
"""Alta3 Research
All in one Django settings to drive Djanjo webserver
Includes a simple home endpoint and a matching
'view' within urlpatterns"""

# python3 -m pip install django
from django.urls import re_path
from django.http import HttpResponse

DEBUG = True                            # verbose output and prevent config of
                                        # ALLOWED_HOSTS variable

SECRET_KEY = 'Youcandanc3youcanjiv3'    # required for a django app

ROOT_URLCONF = __name__                 # The path to the URIs (called URLs here) with the 'views' in
                                        # the project. The var __name__ means "look in this file"

def home(request):
    return HttpResponse('Welcome to the Alta3 App\'s Homepage!')   # send back an HTTP 200

# now we have urlpatterns to defined
# regex r'^$' matches "nothing" and points to the function "home"
urlpatterns = [
    re_path(r'^$', home),
]

