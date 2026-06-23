# Agenda
Agenda de contactos

## 1. Crear un entorno virtual (Virtual Environment)
Crear un entorno virtual para las pruebas de ejecion
````shell
python3 -m venv .venv
````

## 2. Iniciar el entorno virtual
Iniciar el entorno virtual en la terminal para instalar las librerias necesarias
````shell
source .venv/bin/activate
````

## 3. Se descarga, instala o actualiza el instalador de paquetes oficial de python
Se debe de actualizar el instalador de los paquetes de python a la ultima version
````shell
pip install --upgrade pip
````

## 4. Instalacon de micro-framework
Se debe de instalar el micro-framework *web.py* el cual nos sirve para la creacion de aplicaciones web con python, se emplea pip
````shell
pip install web.py
````

## 5. Creacion de archivo requeriments.txt
Este archivo tiene la informacion sobre las versiones de las librerias utiilizadas. Freeze toma una ss y los mete en un archivo .txt
````shell
pip freeze > requeriments.txt
````

## 6. Creacion de archivo runtime.txt
A diferencia de el archivo requeriments.txt, este guarda la informacion sobre las versiones exactas de la herramienta utilizada, en este caso python3. La -V mayuscula es la bandera que nos muestra la version exacta.
````shell
python3 -V > runtime.txt
````

## 7. Creacion del archivo .gitignore
En este archivo se adjuntan todos los archivos privados o de controladores que no deben de ser publicados o archivos que simplemente se deben de ignorar. Los siguientes son los tipicos. *(El archivo .gitignore se debe de realizar antes del primer commit o se publicara todo el codigo sin discriminacion)*
````shell
*.pyc
_pycache_/
.venv
````

## 8. Preparar los archivos creados, moodificados y eliminados del repositorio (Idexar)
Se preparan (escanean) todos los archivos del repositorio para el commit. Paso 1
````shell
git add .
````

## 9. Crear punto de control, guarado o salvado (commit)
Se agregan todos los archivos escaneados anteriormente a un chekpoint con el nombre  asignado
````shell
git commit -m "xxxxxxx [nombre del commit]"
    Existen 3  tipos de commit:
    - CREATED
    - UPDATE
    - FIXED 
````

## 10. Sincronixacion del commit con el repositorio (update final)
Este paso sincroniza los cambios realiizados en el codespace y la nube
````shell
git push -u origin main
````