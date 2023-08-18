#!/usr/bin/python3

from django.http import JsonResponse    # replaces "import json"
from django.http import HttpResponse

def schools(request):
    response_data = {}
    response_data['xmen'] = 'school for gifted youngsters'
    response_data['wizards'] = 'hogwarts school'
    response_data['vampires'] = 'forks high school'
    return JsonResponse(response_data)  # abstraction to return json

# /?universe=marvel /?universe=dc
def readparams(request):

    response_data = {}

    universe = request.GET.get('universe', 'no universe found')
    response_data['universe'] = universe
    
    if universe == 'marvel':
        response_data['storm'] = 'control weather'
        response_data['cyclops'] = 'energy weapon (eye)'
        response_data['gambit'] = 'potential to kinetic energy'
    elif universe == 'dc':
        response_data['batman'] = 'expensive gadgets'
        response_data['superman'] = 'super everything'
        response_data['gambit'] = 'potential to kinetic energy'
        
    return JsonResponse(response_data)  # abstraction to return json
