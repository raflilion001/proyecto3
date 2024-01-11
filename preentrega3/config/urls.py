
from django.contrib import admin
from django.urls import include,path
from .views import saludo,saludo2,nombre,fecha_hora,tirar_dado

urlpatterns = [
    path('admin/', admin.site.urls),
    #path ('saludo/',saludo),
    #path ('saludo2/',saludo2),
    #path("nombre/<nombre>/<apellido>",nombre),
    #path ('fecha_hora/', fecha_hora),
    #path ('tirar_dado/', tirar_dado),
    path ('',include("core.urls")),
    #en include se pone el nombre de la applicacion y el nombre del modulo 
    
    path ('Clientess',include("cliente.urls")),#nombre de la aplicaion (cliente) y el modulo que es urls
        
      
]
