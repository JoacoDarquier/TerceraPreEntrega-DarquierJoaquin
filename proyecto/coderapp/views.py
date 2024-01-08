from django.shortcuts import render
from django.http import HttpResponse

from coderapp.models import *
from coderapp.forms import *



def index(request):
    return render(request, 'index.html')


def pelicula_formulario (request):
    if request.method == "POST":
        formulario = PeliculaFormulario(request.POST)
        print(f" is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data
            nombre = datos.get("nombre")
            genero = datos.get("genero")
            director = datos.get("director")
            pelicula = Pelicula(nombre=nombre, genero=genero, director=director)
            pelicula.save()       
            return render(request, "index.html")   
    else:
        formulario = PeliculaFormulario()
    return render(request,'pelicula_formulario.html', {"formulario": formulario})


def serie_formulario (request):
    if request.method == "POST":
        formulario = SerieFormulario(request.POST)
        print(f" is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data
            nombre = datos.get("nombre")
            genero = datos.get("genero")
            plataforma = datos.get("plataforma")
            cantidadDeCapitulos = datos.get("cantidadDeCapitulos")
            serie = Serie(nombre=nombre, genero=genero, plataforma=plataforma, cantidadDeCapitulos=cantidadDeCapitulos)
            serie.save()       
            return render(request, "index.html")   
    else:
        formulario = SerieFormulario()
    return render(request,'serie_formulario.html', {"formulario": formulario})


def libro_formulario (request):
    if request.method == "POST":
        formulario = LibroFormulario(request.POST)
        print(f" is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data
            nombre = datos.get("nombre")
            genero = datos.get("genero")
            escritor = datos.get("escritor")
            libro = Libro(nombre=nombre, genero=genero, escritor=escritor)
            libro.save()       
            return render(request, "index.html")   
    else:
        formulario = LibroFormulario()
    return render(request,'libro_formulario.html', {"formulario": formulario})


def buscar(request):
    formulario = PeliculaBusqueda()
    return render(request, 'busqueda_pelicula.html', {"formulario": formulario})

def busqueda_pelicula (request):
    if request.method == 'GET':
        pelicula = request.GET.get("nombre")
        if pelicula is None:
            return HttpResponse("Debe cargar una pelicula")
        pelicula = Pelicula.objects.filter(nombre=pelicula)

    return render (request, 'pelicula_busqueda_respuesta.html', {"pelicula": pelicula})






