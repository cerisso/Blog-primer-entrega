from django.urls import path
from .views import crear_posteo, inicio, perfil, vista_posteos, buscar_usuario

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('mi_perfil/', perfil, name="Perfil"),
    path('posteos/', vista_posteos, name="Posteos"),
    path('buscar-usuario/', buscar_usuario, name="Buscar usuario"),
    path('crear-posteo/', crear_posteo, name="Crear posteo"),
    ]