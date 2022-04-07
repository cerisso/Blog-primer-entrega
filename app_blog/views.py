from django.shortcuts import render
from app_blog.templates.forms import PosteoForm, BuscarUsuarioForm
from .models import Posteos, Usuarios, Categorias

# Create your views here.
def inicio(request):
    categoria = Categorias.objects.all()
    return render(request, 'app_blog/index.html', {"categoria": categoria})

def perfil(request):
    categoria = Categorias.objects.all()
    return render(request, 'app_blog/perfil.html', {"categoria": categoria})

def vista_posteos(request):
    posteos = Posteos.objects.all()
    categoria = Categorias.objects.all()
    return render(request, 'app_blog/posteos.html', {"posteos": posteos, "categoria": categoria})

def crear_posteo(request):
    posteos = Posteos.objects.all()
    categorias = Categorias.objects.all()
    formulario = PosteoForm()
    #Cuando se envían los datos entra a POST
    if request.method == 'POST':
        form = PosteoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            posteos = Posteos(content=data['contenido'],author=data['autor'])
            posteos.save()
            return render(request, 'app_blog/crearPosteo.html', {'formulario': formulario, "categorias": categorias})
    #Cuando hay un get
    else :
        return render(request, 'app_blog/crearPosteo.html', {'formulario': formulario, "categories": categorias})

def buscar_usuario(request):
    buscarUsuarioForm = BuscarUsuarioForm()
    categorias = Categorias.objects.all()
    data = request.GET.get('usuario', "")
    if data:
        print(data)
        form_with_data = BuscarUsuarioForm(request.GET)
        if form_with_data.is_valid():
            perfil = Usuarios.objects.filter(user=data).first()
            print (perfil)
            if (perfil):
                return render(request, 'app_blog/buscar_usuario.html', {"buscar_usuario": buscarUsuarioForm,"usuario": perfil})
            return render(request, 'app_blog/buscar_usuario.html', {"buscar_usuario": buscarUsuarioForm,"usuario": None})

        return render(request, 'app_blog/buscar_usuario.html', {"buscar_usuario": buscarUsuarioForm, "usuario": perfil, "error": form_with_data.errors})
    
    return render(request, 'app_blog/buscar_usuario.html', {"buscar_usuario": buscarUsuarioForm, "usuario": None, "error": None, "categorias": categorias})