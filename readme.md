# App de introducción a Flask

Hello World en Python con Flask

## Instalación

- En el entorno de python, ejecutar el comando

```
pip install -r requirements.txt
```

La libreria utilizada: flask https://flask.palletsprojects.com/en/2.2.x/

## Ejecución del programa

Para inicializar el servidor:

- Windows: `set FLASK_APP=hello.py`
- Mac: `export FLASK_APP=hello.py`

## Comando para ejecutar el servidor

```
flask --app hello run
```

## Comando para ejecutar el servidor en otro puerto

```
flask --app hello -p run 5001
```

## Actualizar el servidor con cambios en tiempo real

```
flask --app hello --debug run
```
