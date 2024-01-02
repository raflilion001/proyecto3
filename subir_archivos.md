primero iniciamos en la terminal (por unica vez el )get init

segundo para pasar los cambios de la work area a la stage area ultilizamos el (git add README.md )o de forma manual con el mas

luego pasamos al area de repositorio en la nuve (tomamos la foto) con (git commit -m "nombre desriptivo del cambio")

(git remote and origin http.direccion del repositorio en git)  agrega la url del repositorio donde enviaremos las cosas solo deberia hacerse una vez  

empujamos (por unica vez) tambien a la nuve con git push -u origin NombreDeLaRama


resumen los que deberemos usar continuamente son:

git add README.md

git commit -m "foto"

git branch -M main crea una rama y reemplazamos el main por el nombre que quieramos darle

git push

git checkout nombre de la rama en la que queremos posicionarnos  

git merge Rama_A_Fusionar : para fusionar una rama me posiciono en la rama principal  y en la terminal invoco el comando git merge seguido de la rama que quiero fucionar esto guardaria los cambios a la stage area  comun entre las dos ramas y se subira a internet como una foto comun que comparten ambas ramas creando un punto de guardado para ambas  con git push
