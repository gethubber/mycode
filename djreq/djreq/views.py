#!/usr/bin/python3

import pprint
from django.http import HttpResponse
from django.core import serializers
import json


# python3 -m pip install requests
import requests

# python3 -m pip install Django
from django.http import JsonResponse    # replaces "import json"

# API to lookup - Django will proxy the request for us
API = "http://api.open-notify.org/astros.json"
    
# https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
APINASA = "https://api.nasa.gov/planetary/apod?api_key="

# Your NASA API key goes here
# in production this should be set as an environmental variable
APIKEY = "DEMO_KEY"

def astro(request):    
    res = requests.get(API)
    return JsonResponse(res.json(),json_dumps_params={'indent': 2})  # abstraction to return json
    if pretty:
        output = json.dumps(json.loads(output), indent=4)
    return HttpResponse(output, content_type="application/json")

def nasa(request):
    res = requests.get(f"{APINASA}{APIKEY}")
    return JsonResponse(res.json(), json_dumps_params={'indent': 2}) # abstraction to return json
    if pretty:
        output = json.dumps(json.loads(output), indent=4)
    return HttpResponse(output, content_type="application/json")



