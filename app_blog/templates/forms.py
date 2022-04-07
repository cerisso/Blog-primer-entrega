from django import forms

class PosteoForm (forms.Form):
    contenido = forms.CharField(max_length=4000)
    autor = forms.CharField(max_length=100)

class BuscarUsuarioForm (forms.Form):
    Usuarios = forms.CharField(max_length=100)
