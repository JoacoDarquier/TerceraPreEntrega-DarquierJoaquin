from django.urls import path, include
from coderapp.views import (
    index, 
    pelicula_formulario, 
    serie_formulario, 
    libro_formulario, 
    busqueda_pelicula, 
    buscar)

urlpatterns = [
    path('peliculaFormulario/', pelicula_formulario, name = 'pelicula_formulario'),
    path('serieFormulario/', serie_formulario, name = 'serie_formulario'),
    path('libroFormulario/', libro_formulario, name = 'libro_formulario'),
    path('busquedaPelicula/', buscar, name = 'busqueda_pelicula'),
    path('buscar/', busqueda_pelicula, name = 'pelicula_busqueda_respuesta'),
    path('', index, name = 'index'),
]