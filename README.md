 # ***Biblioteca de películas*** #

Pequeña biblioteca de almacenamiento de Películas creada en Django   
  
  
## Instalación ##
Primero clonamos el Repositorio (también podemos descargar el repositorio en formato ZIP):  
  
```  
git clone https://github.com/AlbertoMaciasGutierrez/biblioteca.git  
```
  
  
Una vez descargado el repositorio debemos de instalar los requirements.txt en nuestro entorno virtual:  
  
```  
pip install -r requirements.txt  
```
  
Para poder hacer uso de la aplicación necesitamos tener instalado MariaDB. Una vez instalado esto, desde un terminal o bien desde el programa HeidiSQL (el cual se instala al instalar MariaDB) creamos una base de datos con la orden:  
```  
CREATE database nombreBaseDatos  
```
  
Ahora acccedemos a la base de datos creada en la que registramos un usuario y le damos permisos para que pueda acceder a la base de datos:  
```  
CREATE USER nombreUsuario@localhost IDENTIFIED BY 'contraseña';
GRANT ALL privileges ON nombreBaseDatos.* TO nombreUsuario@localhost;
FLUSH PRIVILEGES; 
```  
  
Por último para poder usar la base de datos en nuestro proyecto Django, debemos de cambiar una parte del código en el fichero ***"biblioteca/settings.py"***:  
```  
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombreBaseDatos',
        'USER': 'nombreUsuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```  
- En la parte de *'NAME'*, introducimos el nombre de la base de datos
- En la parte de *'USER'*, introducimos el nombre del usuario creado  
- En la parte de *'PASSWORD'*, introducimos la contraseña del usuario creado
- En la parte de *'PORT'*, introducimos el número de puerto en el que se lanzan las bases de datos de MariaDB (3306 por defecto)
  
  ---
  
  
## Ejecución del proyecto ##
Accediendo dentro del directorio del proyecto al mismo nivel que se encuentra el documento "manage.py", abrimos un terminal y migramos los modelos a la base de datos:  
```  
python manage.py migrate  
```    
Una vez realizado esto ya podemos lanzar el servidor Django:
```  
python manage.py runserver --insecure  
```  
Lanzamos en este modo el proyecto porque tenemos el depurador desactivado pero seguimos usando archivos estáticos 

Para poder disponer de la funcionalidad de la biblioteca debemos de acceder a la dirección http://127.0.0.1:8000/pelicula. Si accedemos a una página que no existe el proyecto nos redirige a una página de error personalizada.  
  
![ScreemShot](https://raw.githubusercontent.com/AlbertoMaciasGutierrez/biblioteca/main/img/Inicio.png)  
  
  ---
  
  
  
## Ejemplo de uso en web ## 
Para poder usar esta biblioteca debemos de tener una cuenta. Para registrar una cuenta clicamos arriba a la derecha en la barra de navegación en ***"Registrar"*** o debajo del botón ingresar en ***"Registrar cuenta"***.  

Rellenamos el formulario con el nombre de usario (con el que se accederá posteriormente a la cuenta), email, nombre, apellido, y contraseña. Cuando tengamos esto clicamos en el botón ***"Save"***. Cuando nos registremos nos llevará a la página donde se encuentra la biblioteca de películas. Clicando en la barra de arriba en ***"Biblioteca de Películas"***, ***"Directores"*** o ***"Actores"***, podremos acceder al listado de cada uno de estos elementos que hay guardados en la biblioteca (en este paso si accedes a estos listados no habrá ningún actor, película o director).   
  
Para añadir una nueva película clicamos en el símbolo de ***"+"*** (antes de añadir una película debemos de añadir previamente un director y como mínimo un actor), sale un formulario donde rellenamos los datos de dicha película y podemos elegir un director de los previamente introducidos y de uno a muchos actores para el reparto (para añadir un director o actor se hace de manera similar). Cuando damos al botón confirmar la página nos redirige a los detalles de la película introducida, se debe ver algo como esto:  
  
![ScreemShot](https://raw.githubusercontent.com/AlbertoMaciasGutierrez/biblioteca/main/img/Pelicula.png)  
  
Si clicamos en el link del director la página nos redirige hasta los detalles de este. Lo mismo ocurre con los actores en el apatado **"Reparto"**. Además si clicamos en el lápiz amarillo podemos editar la película, en la cruz roja podemos borrar la película y en el corazón verde podemos valorar la película con una nota de 0-10 (los botones de edición y borrado también se encuentran en los actores y directores).  
  
A medida que introduzcamos películas, actores y directores el listado de estos irá creciendo. Se debe ver algo como esto:  
  
![ScreemShot](https://raw.githubusercontent.com/AlbertoMaciasGutierrez/biblioteca/main/img/Peliculas.png)

  
Colocandose en el listado de película podemos buscar cualquier película mediante el buscador de la barra de navegación, lo mismo ocurre para los actores y directores si nos situamos en los respectivos listados. 

Por último clicando en el icono de navegación situado arriba a la derecha en la barra de navegación, se abre un desplegable y si pulsamos en la parte de ***"Cerrar Sesión"***, cerraremos la sesión de nuestra cuenta.  
  
  ---  
    
## Ejemplo de uso en api REST ##
Del mismo modo que para poder utilizar el proyecto en web, debemos de tener una cuenta e iniciar sesión en esta.  
Para poder ver el listado de actores, películas o directores tenemos que acceder a:  http://127.0.0.1:8000/api/actores, http://127.0.0.1:8000/api/directores y http://127.0.0.1:8000/api/peliculas. Además de poder ver el listado de los distintos elementos de la biblioteca, también podremos añadir más elementos mediante ***"POST"***.  
Si añadimos a las URLs anteriormente mencionadas, el *"id"* de cada elemento al final, accederemos a la configuración en concreto de cada uno de estos. Una vez dentro de cada elemneto, podremos actualizar cada uno de estos mediante ***"PUT"*** o borrar mediante ***"DELETE"***.  
Dentro de cada película, si además añadimos al final de la URLs la palabra *"valorar"*, podremos votar a una película con una nota de 0.0 a 10.0. En este caso la forma de introducir una valoración es la siguiente:  
  
```  
{
    "valoracion": 7.0
}
```  


