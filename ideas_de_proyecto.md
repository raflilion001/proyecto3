Crear una forma de que  el cliente pueda ingresar sus datos y se guarden para posteriormente poder acceder a los mismos ingresando nombre y apellido 

creo que creando unos inputs en una lista que guarden los datos en un diccionario y a su vez estos se guarden en un json 
----------
import json

archivo= open ("mi_json_creado.json", "r") #para que no se borren los datos del cliente cargamos antes de crear el diccionario vacio en modo lectura "r"

clientes= json.load(archivo) # gracias a estaas dos lineas de codigo qeu agregamos  no aran falta las dos siguientes

#clientes={}

#clientes["cliente"] = []

nombre= input("nombre : ")

edad = int(input("edad : "))

formulario= {"nombre":nombre, "edad":edad}

clientes["clientes"].append(formulario)  #clientes llama a la clave clientes que esta entre corchetes la cual es una lista , el (.append) para qeu abra  lo que tiene entre parentecis en este caso el formulario
 
archivo= open ("mi_json_creado.json", "w") #con esta opcion guardamos los cambios

json.dump(clientes,archivo,indent = 4) #convierto  un objeto python a una cadena json y requiere de un objeto (clientes), un archivo (archivo) y si deseamos que tenga una identacion  colocamos el parametro indent= al numedo de indentaciones requeridas

archivo.close()
-------