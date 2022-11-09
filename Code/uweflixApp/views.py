from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import datetime

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'uweflixApp/index.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )