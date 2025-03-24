""" • ¿Qué es GitHub?
Es un servicio que aloja repositorios remotos

• ¿Cómo crear un repositorio en GitHub?
Se creo un repositorio en github (despues de crear un usuario y loguearse), se hace click en el simbolo +

• ¿Cómo crear una rama en Git?
Usando el comando git branch nombre_rama

• ¿Cómo cambiar a una rama en Git?
Con el comando git checkout nombre_rama

• ¿Cómo fusionar ramas en Git?
Con el comando git merge nombre_rama

• ¿Cómo crear un commit en Git?
Con el comando git commit -m "mensaje descriptivo sobre los cambios realizados"

• ¿Cómo enviar un commit a GitHub?
Con el comando git push -u origin nombre_rama primero y luego con el comando git push

• ¿Qué es un repositorio remoto?
Es la copia de un repositorio local que se encuentra en un servidor remoto

• ¿Cómo agregar un repositorio remoto a Git?
Primero se inicializa git con git init, despues se agrega el contenido con git add ., como tercer paso se realiza el git commit  -m "descripcion", luego se agrega el repositorio remoto con git remote add origin url_repositorio y por ultimo se envia el contenido con git push -u origin master.

• ¿Cómo empujar cambios a un repositorio remoto?
Con el comando git push -u origin master

• ¿Cómo tirar de cambios de un repositorio remoto?
Con el comando git pull

• ¿Qué es un fork de repositorio?
Es cuando realizamos la copia de un repositorio de un tercero, lo copiamos bajo nuestro usuario para poder realizarle cambios.

• ¿Cómo crear un fork de un repositorio?
Arriba a la izquierda del repositorio que queremos copiar hacemos click en el boton fork

• ¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?
Hacemos click en el boton pull request y luego en el boton new pull request

• ¿Cómo aceptar una solicitud de extracción?
Hacemos click en el boton merge pull request

• ¿Qué es un etiqueta en Git?
Es una forma de marcar un punto en la historia de un repositorio

• ¿Cómo crear una etiqueta en Git? 
Con el comando git tag -a nombre_etiqueta -m "descripcion"

• ¿Cómo enviar una etiqueta a GitHub?
Con el comando git push origin nombre_etiqueta

• ¿Qué es un historial de Git?
Es el registro de todos los cambios que se han realizado en un repositorio

• ¿Cómo ver el historial de Git?
Con el comando git log

• ¿Cómo buscar en el historial de Git?
Con el comando git log --grep="palabra_buscada"

• ¿Cómo borrar el historial de Git?
Con el comando git reset --hard

• ¿Qué es un repositorio privado en GitHub?
Es un repositorio que no es visible para el publico, se selecciona la opcion al principio de la creacion del repositorio

• ¿Cómo crear un repositorio privado en GitHub?
De la misma forma que se crea un repositorio pero seleccionando la opcion de privado

• ¿Cómo invitar a alguien a un repositorio privado en GitHub?
En la pestaña settings del repositorio seleccionamos la opcion de collaborators y agregamos el usuario

• ¿Qué es un repositorio público en GitHub?
Es un repositorio que es visible para el publico

• ¿Cómo crear un repositorio público en GitHub?
De la misma forma que se crea un repositorio privado, pero esta vez seleccionando la opcion de publico

• ¿Cómo compartir un repositorio público en GitHub? 
Compartiendo el link del repositorio, que esta en la barra del navegador"""