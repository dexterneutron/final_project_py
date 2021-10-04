from django.shortcuts import render
from django.http import HttpResponse

import requests
from requests.models import HTTPError


def index(request):
    return HttpResponse("Here is gonna be my reader view")

def feed(request):
    url = 'http://127.0.0.1:5000/api/feed'
    response = requests.get(url)

    return HttpResponse(response)
