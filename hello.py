from flask import Flask, render_template #1-Importar librería (y funciones específicas de ser necesario)

app = Flask(__name__) #2- Instancia de la clase que inicializa flask

@app.route("/hola") #3- Ruta que indica con cual URL se ejecuta la función
def hola_mundo():
	return "Hola mundo Flask"

@app.route("/adios")
def despedida():
	return "Hasta pronto, Persona"

#Ejecutando el servidor
#	Copiar el url del puerto en el navegador, seguido de /'ruta indicada en app.route'


#Enviar parámetros en las rutas
@app.route("/nombre/<n>")
def name(n):
	return f'Tu nombre es {n}'


#Se puede asignar tipo de parámetro en la ruta (int:, float:, path:, str:)
@app.route("/numero/<int:n>")
def cuadrado(n): 
	return f'El cuadrado de {n} es {n*n}'


#Devolviendo un HTML
@app.route("/operaciones/<int:n1>/<int:n2>/<ope>")
def calculadora(n1,n2, ope):
	if ope == 'sum':
		return render_template('hola.html', resultado=f'La suma de {n1} y {n2} es {n1+n2}')
	elif ope == 'res':
		return render_template('hola.html', resultado=f'La resta de {n1} y {n2} es {n1-n2}')
	elif ope == 'mult':
		return render_template('hola.html', resultado=f'La multiplicación de {n1} y {n2} es {n1*n2}')
	elif ope == 'div':
		return render_template('hola.html', resultado=f'La división de {n1} y {n2} es {n1/n2}')

'''
@app.route("/primerhtml")
def callhtml():
	return render_template("hola.html")

@app.route("/primerhtml/<nombre>")
def callhtml(nombre):
	return render_template("hola.html",name=nombre)
'''