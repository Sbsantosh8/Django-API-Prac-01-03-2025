import requests
from django.shortcuts import render

# API URL
api_url = "http://127.0.0.1:8000/"


def index(request):

    return render(request, "home.html")
