from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'ports/index.html')

def skdue(request):
    return render(request, 'ports/skdue.html')
