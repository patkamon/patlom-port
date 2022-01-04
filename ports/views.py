from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = "Hello, world. You're at the polls index."
    return render(request, 'ports/index.html')
