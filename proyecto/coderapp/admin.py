from django.contrib import admin

# Register your models here.

from coderapp.models import Pelicula, Libro, Serie

admin.site.register(Pelicula)
admin.site.register(Libro)
admin.site.register(Serie)
