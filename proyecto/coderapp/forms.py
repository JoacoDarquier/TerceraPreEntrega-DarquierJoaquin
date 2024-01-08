from django import forms

class PeliculaFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    genero = forms.CharField(max_length=20, required=False)
    director = forms.CharField(max_length=20, required=False)

class LibroFormulario (forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    genero = forms.CharField(max_length=20, required=False)
    escritor = forms.CharField(max_length=20, required=False)

class SerieFormulario (forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    genero = forms.CharField(max_length=20, required=False)
    plataforma = forms.CharField(max_length=20, required=False)
    cantidadDeCapitulos = forms.IntegerField()

class PeliculaBusqueda (forms.Form):
    nombre = forms.CharField(max_length=20)


