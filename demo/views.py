from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    response = requests.get('https://jsonplaceholder.typicode.com/photos')
    posts = response.json()
    for a in posts:
        print(a["id"])
    return render(request, 'index.html',{"posts":posts})
