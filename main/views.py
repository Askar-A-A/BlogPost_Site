from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'main page',
        'values': ['Something', 'Hello', "123"]
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacs(request):
    return render(request, 'main/contacs.html')
