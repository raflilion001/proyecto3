from django.shortcuts import render

from .models import Cliente

# Create your views here.


def index(request):
    clientes = Cliente.objects.all()
    return render(request, "cliente/index.html",{"clientes":clientes})

# primer argumento un request,segundo el
#nombre de la carpeta contenedora /y el template, el contexto en forma de diccionario con un valor de instancia 
#que en este caso es la variable  clientes

#de esta forma le pasamos al html todo el contenido de la base de datos de este modelo   
#