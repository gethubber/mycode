# NEW - standard library imports go on top
import datetime    # NEW

# imports from Django
from django.shortcuts import render
from django.http import HttpResponse

# This view will return "Welcome to the Phoenix Cafe!" as text
def welcome(request):
    return HttpResponse("Welcome to the Phoenix Cafe!")


# your custom code will be here


# NEW - new view that returns the current date and time
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)  # we are not returning a static string

