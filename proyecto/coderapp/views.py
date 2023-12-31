from django.shortcuts import render
from django.http import HttpResponse

# from coderapp.models import *


def index(request):
    return render(request, 'index.html')
