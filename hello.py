from flask import Flask #1-Importar librería

app = Flask(__name__) #2- Instancia de la clase que inicializa flask

@app.route("/hola") #3- Ruta que indica con cual URL se ejecuta la función
def hola_mundo():
	return "Hola mundo Flask"

@app.route("/adios")
def despedida():
	return "Hasta pronto, Persona"

#Para inicializar el servidor:
#	Windows: set FLASK_APP=hello.py
#	Mac: export FLASK_APP=hello.py

#Ejecutar el servidor
#	flask --app hello run
#	Copiar el url del puerto en el navegador, seguido de /'ruta indicada en app.route'
#	Si el puerto 5000 está ocupado: flask --app hello -p run 5001

#Para actualizar el servidor con cambios en tiempo real:
#	flask --app hello --debug run