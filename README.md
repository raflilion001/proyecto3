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

py -m venv .venv          

.venv\Scripts\activate    #activador de entorno virtual

crear un archivo .gitignore 

que contenga en su primera linea .venv para que esa carpeta no sea seguida por git a la hora de subir a la nuve


instalar django:
pip install django
creando proyecto: 
django-admin startproject config .
django-admin --version

creando aplicacion: 
django-admin startapp core
-------------------------------------------------------------------------------------
py manage.py makemigrations = Este comando examina los modelos actuales y compara su estado con las migraciones existentes para determinar qué cambios deben aplicarse.

python manage.py migrate  = Este comando ejecutará las migraciones pendientes y actualizará la base de datos de acuerdo con los cambios en tus modelos.

En resumen, makemigrations es la primera etapa en el proceso de actualización de la base de datos en Django. Crea archivos de migración basados en los cambios en tus modelos, y luego migrate aplica esos cambios en la base de datos.

py manage.py createsuperuser = Crea un super usuario despues vamos a admin importamos la clase cliente y pais desde el modulo models con importacion relativa

py manage.py check NombreDeLaAplicacion = sirve para checkear que no haya problemas con la aplicacion que creamos

py manage.py sqlmigrate NombreDeLaAplicacion 0001 = Cuando ya tenemos la base de datos pero aun está vacia usamos este comando para generar su estructura# Penultima_practica
