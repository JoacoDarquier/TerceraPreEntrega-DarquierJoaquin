from django.urls import path, include
from coderapp.views import index

urlpatterns = [
    path('', index, name = 'index')
]