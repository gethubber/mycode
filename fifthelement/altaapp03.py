#!/usr/bin/python3
"""Alta3 Research
All in one Django settings to drive Djanjo webserver

Includes a simple home endpoint and a matching
'view' within urlpatterns

The color of the heading may be scraped via ?color=<color>
Example:
127.0.0.1:8000/?color=green
127.0.0.1:8000/?color=purple"""

# python3 -m pip install django
from django.urls import re_path
from django.http import HttpResponse

DEBUG = True                            # verbose output and prevent config of
                                        # ALLOWED_HOSTS variable

SECRET_KEY = 'Youcandanc3youcanjiv3'    # required for a django app

ROOT_URLCONF = __name__                 # The path to the URIs (called URLs here) with the 'views' in
                                        # the project. The var __name__ means "look in this file"

# return an HTML template
def home(request):
    """return a template to any lookups to home with optional color"""

    # NOTE: The following directly snags input directly from the URIs
    # user input should always be scrutinized to avoid security issues like XSS
    color = request.GET.get('color', '')   # scrape out the parameter from ?color=<color>

    return HttpResponse(
        '<h1 style="color:' + color + '">Welcome to the Alta3 App\'s Homepage!</h1>'
    )  # don't use user input like that in real projects!

urlpatterns = [
    re_path(r'^$', home),
]

