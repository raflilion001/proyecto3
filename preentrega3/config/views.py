from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request):
    
    return HttpResponse("hola")

def saludo2(request):
    
    nombre = input("ingresa tu nombre : ")
    
    return HttpResponse(f"Hola <h1>{nombre}</h1>")

def nombre(request,nombre,apellido):
    
    return HttpResponse(f"{apellido.upper()}, {nombre}")

def fecha_hora(request):
    from datetime import datetime
    ahora = datetime.now().strftime(r"%d/%m/%Y %H:%M:%S.%f")# srtftime sirve para colocar dias meses y años
    
    return HttpResponse(ahora)

def tirar_dado(request): 
    import random   
    tirada = random.randint(1,6)
     
    if tirada == 6:
         return HttpResponse (f"felicitaciones tiraste un dado: {tirada} ganaste ")    
     
     #en lugar de usar print usamos el return httpresponse
     
    else:
         return HttpResponse (f"tiraste un dado: {tirada} vuelve a intentar")
        
   
             
    
  
          