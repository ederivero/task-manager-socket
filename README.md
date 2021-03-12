# <div align="center">Webinar Task Manager BackEnd</div>

Bienvenido a mi repositorio 📂️ donde podrás encontrar el codigo del webinar de **Task Manager con Sockets** 🤓️

Para comenzar es muy sencillo solamente sigue los siguientes pasos de instalación y podrás ejecutar el proyecto en tu máquina 💻️! 🤩️🤩️

## Instalación

Este repositorio requiere que tengas instalado [Python](https://www.python.org/) v3.7+ para funcionar.
Una vez que tengas python instalado, para comprobar corre el siguiente comando en una _terminal_ o _power shell_
**Nota:** Si estas usando Mac o Linux ya tienes instalado Python🐍️

```
$ python --version
```

Ahora descarga el repositorio y luego creemos un entorno virtual dentro de la carpeta descargada: 🤓️

```
$ python -m venv entorno
```

Esto creará una carpeta con el nombre _entorno_ y ahí se instalarán todas las librerias necesarias de nuestro proyecto.

Luego abramos una terminal (o podemos usar la que ya teníamos anteriormente) y nos ubicamos dentro de la carpeta descargada y procederemos a levantar el entorno virtual

- Para Windows:
  - cmd
  ```
  $ entorno/Scripts/activate
  ```
  - powershell
  ```
  $ entorno/Scripts/activate.ps1
  ```
- Para Mac / Linux:

    ```
    $ source entorno/bin/activate
    ```
Luego de haber activado el entorno virtual instalaremos las librerias a usar usando el archivo _requirements.txt_ 📄️
```
$ pip install -r requirements.txt
```
Eso comenzará a instalar toodas las librerias necesarias para nuestro proyecto 🌟️

Ya estámos! Ya podemos levantar nuestro proyecto, no necesitas preocuparte de las bases de datos 🗄️ ya que estamos usando [SQLITE](https://www.sqlite.org/index.html) que es una base de datos muy ligera.

Para levantar nuestro proyecto de BackEnd debemos ejecutar el siguiente comando
**Nota:** Asegurate de estar en el entorno virtual sino dará error de librerias.

```
$ python app.py
```

Y ya ya estamos! Nuestro proyecto ha sido levantado exitosamente 🚀️🚀️🚀

## Extras

Si quieres visualizar los datos que se han almacenado en la base de datos, te recomiendo descargarte el siguiente software ultra ligero ➡️ [SQLite Browser](https://sqlitebrowser.org/dl/)

## Licencia

[MIT](https://opensource.org/licenses/MIT)

**Software Libre, Hell Yeah!🤙️🤙️**

