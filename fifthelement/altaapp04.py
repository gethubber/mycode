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

# engage django templating engine (more a less, jinja)
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates'},]

# return an HTML template
def home(request):
    """return a template to any lookups to home with optional color"""

    # NOTE: The following directly snags input directly from the URIs
    # user input should always be scrutinized to avoid security issues like XSS
    color = request.GET.get('color', '')   # scrape out the parameter from ?color=<color>

    return HttpResponse(
        '<h1 style="color:' + color + '">Welcome to the Alta3 App\'s Homepage!</h1>'
    )  # don't use user input like that in real projects!



from django.template import engines
from django.template.loader import render_to_string

def about(request):
    title = 'Alta3App'
    author = 'RZFeeser'

    # Django templating engine is very close to Jinja templating
    about_template = '''<!DOCTYPE html>
    <html>
    <head>
      <title>{{ title }}</title>
    </head>
    <body>
      <h1>About {{ title }}</h1>
      <p>This Website was developed by {{ author }}.</p>
      <p>Now using the Django's Template Engine.</p>
      <p><a href="{% url 'homepage' %}">Return to the homepage</a>.</p>
    </body>
    </html>
    '''

    django_engine = engines['django']
    template = django_engine.from_string(about_template)
    html = template.render({'title': title, 'author': author})

    return HttpResponse(html)

# match on "nothing" for the homepage
# math on "about/" for the about page
urlpatterns = [
    re_path(r'^$', home, name='homepage'),
    re_path(r'^about/$', about, name='aboutpage'),
]
  
