# proyecto3


creando repositorio:

echo "# Penultima_practica" >> README.md
git init
git add README.md
git commit -m "first commit" # lo que esta entre comillas sera el nombre con el que se guardara la foto
git status
git log
git log --oneline
git branch -M main
git remote add origin http://github.com
git branch -m dev
git push -u origin main  #Puedes enviar tus cambios al repositorio remoto utilizando el comando
git checkout dev o main
git merge dev = fusiona
git branch -d dev = eliminar rama
git clone link = para descargar desde github hay que borrarle el git(oculto). que está en la carpeta 
git pull = sirve para traer todo lo que está en la nube

entorno virtual: 

py -m venv .venv   #  crea la carpeta venv .venv     (-m) indica que va ejecutar un modulo de python qeu biene incluido .venv es el argumento que le dare al entorno virtual  se utiliza venv por convencion   

.venv\Scripts\activate    # activador de entorno virtual

crear un archivo .gitignore 

que contenga en su primera linea .venv para que esa carpeta no sea seguida por git a la hora de subir a la nuve
---------------------------------------------

instalar django:
pip install django

creando proyecto: 

django-admin startproject config .    startproject es un comando ,config es el nombre de nuestra carpeta de configuracion y el  ( .) es para qeu lo cree dentro

ls 
django-admin --version

creando aplicacion: 
django-admin startapp core

##
otros comandos:
-creo una carpeta "proyect"
-"cd proyect"
-"django-admin startproject config ." #nos crea una carpeta config
- "python manage.py runserver"

-python manage.py startapp cliente ##crea una carpeta con el nombre cliente

-python manage.py makemigrations  

-python manage.py migrate

python manage.py createsuperuser
-------------------------------------------------------------------------------------
py manage.py makemigrations = Este comando examina los modelos actuales y compara su estado con las migraciones existentes para determinar qué cambios deben aplicarse.

python manage.py migrate  = Este comando ejecutará las migraciones pendientes y actualizará la base de datos de acuerdo con los cambios en tus modelos.

En resumen, makemigrations es la primera etapa en el proceso de actualización de la base de datos en Django. Crea archivos de migración basados en los cambios en tus modelos, y luego migrate aplica esos cambios en la base de datos.

py manage.py createsuperuser = Crea un super usuario despues vamos a admin importamos la clase cliente y pais desde el modulo models con importacion relativa

py manage.py check NombreDeLaAplicacion = sirve para checkear que no haya problemas con la aplicacion que creamos

py manage.py sqlmigrate NombreDeLaAplicacion 0001 = Cuando ya tenemos la base de datos pero aun está vacia usamos este comando para generar su estructura# Penultima_practica
-----------------

httpresponse recibe solo 1 parametro ademas de request  pero podemos agregar mas de uno  con el f string

def nombre(request,nombre,apellido):
    
    return HttpResponse(f"{apellido.upper()}, {nombre}")

----------------------------------
creamos una aplicacion core con el comando:

django-admin startapp core  # puede tener cualqueir nombre  

se crea un paquete con el nombre core

Creamos dentro de core una carpeta llamada TEMPLATE dentro una carpeta llamada como la carpeta qeu contiene a template en este caso core y finalmente dentro de esta un archivo index.html 

index = de forma convencional se utiliza para crear el archivo html

dentro del views de core  creamos las funciones que se importaran a nuestro archivo html

#crea tus vistas

def index(request):
    return render(request,"core/index.html") 


creamos una url haciendo clic derecho sobre el core mas externo , importamos los views y rellenamos los path

from django.urls import path
from.views import index

urlpatterns = [
    path('core/', index),
 
]

tenemos que hacerle saber a django que existe la aplicacion core para qeu sea funcional y para ello nos dirigimos a la carpeta config /settings y buscamos la variable llamada INSTALLES_APPS y agregamos el elemento "core",

luego para devemos agregar en urls de config la importacion includ y :

path ('core/',include("core.urls")),#en include se pone el nombre de la applicacion y el nombre del modulo 

esto lo hacemos ya que config es el programa principal 



---------------

las urls de config son las principales para qeu funcionen las que estan en una app en este caso core necesitamos importarlas 

-para que aparezca primero  un texto en la pagina debemos  colocar en views de la app un diccionario como argumento

pasamos 3 argumentos

def index(request):
    return render(request,"core/index.html",{"nombre":"ferreteria"}) 

-para salir  de git log --oneline precono q
-------------------

para copiar los cambios de una rama otra primero nos posicionamos en la rama que quiereamos agregar los cambios y escribimos el siguiente codigo:

git merge rama_en_la_que_queramos_guardar_los_cambios





--------------------------

<p><a href="{% url 'cliente:index'%}">Ir a Cliente</a></p>  hiper vinculo sirve para llevarme a una determinada app en este caso cliente