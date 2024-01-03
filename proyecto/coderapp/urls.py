from django.urls import path, include
from coderapp.views import index, pelicula_formulario, serie_formulario, libro_formulario

urlpatterns = [
    path('', index, name = 'index'),
    path('peliculaFormulario/', pelicula_formulario, name = 'pelicula_formulario'),
    path('serieFormulario/', serie_formulario, name = 'serie_formulario'),
    path('libro_formulario/', libro_formulario, name = 'libro_formulario'),
]