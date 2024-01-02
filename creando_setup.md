en la misma ubicacion donde creamos el paquete principal  creamos un archivo
setup que contrenga la informacion opcional y  un apartado obligatorio que sera el de
packages= ["nombre de paquete a importar"]

ubicados en la terminal donde se encuentra el paquete y el setup ejecutar "python setup.py sdist"

esto crea un archivo ejecutable que puede ser compartido o instalado en nuestro python, una vez instalado 
puede invocarse y usar cualquier clase (funcion ) contenida en los modulos del paquete  en cualquier lugar de python  