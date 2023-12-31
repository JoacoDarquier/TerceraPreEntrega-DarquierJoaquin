from django.urls import path, include
from coderapp.views import *

urlpatterns = [
    path('', index, name = 'index')
]