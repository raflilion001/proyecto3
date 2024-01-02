nunca nombrar nuestro archivo json solo con el nombre json

json.dumps convierte un diccionario a formato json, para ello lo aremos de la siguiente forma

json.dumps(requiere como argumento oblicatorio un objeto(usaremos cliente que contiene los diccionaros con los datos de los clientes ))

print(json.dumps(clientes)) (devolvera un archivo .json pero no es tan legible en pantalla ya que no toma caracteres no ingleses, si queremos que estos sean legibles deberemos escribirlo de la siguiente forma: )

print(json.dumps(clientes,ensure_ascii=False))  (esto nos permitira visualizar tildes , eñes y otros caracteres )

