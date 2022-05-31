# Importar la biblioteca de flask y librerias necesarias
from tkinter import messagebox
from flask import Flask, redirect, render_template, request, url_for, flash
import pickle

# Instanciar la aplicación
# Nombre por defecto y ruta donde están los modelos
app = Flask(__name__)

##################### CLIENTE #####################
# Arreglo para almacenar datos
registro = []

# 1. Funcion controlador que muestra el registro de un cliente
# Definicion de la ruta por defecto,
@app.route('/')
# Lamar a principal
def home():
    return render_template('index.html', registro=registro)

# 2. Funcion controlador para agregar el registro
# Definicion de la ruta
@app.route('/enviar', methods=['POST'])
# Llamar a enviar
def enviar():
    # Funcion condicional para enviar los datos del formulario
    if request.method == 'POST':

        nombre = request.form['nombre']
        telefono = request.form['telefono']
        estado = request.form['estado']

        # Funcion condicional para no registrar en caso de datos vacios
        if nombre == '' or telefono == '' or estado == '':
            #Mensaje de alerta de campos faltantes
            messagebox.showwarning("¡Alerta!","Ingrese todos los campos")
            return redirect(url_for('home'))

        else:
            #Mensaje de autorizacion de registro
            resultado = messagebox.askquestion("Registrar", "¿Está seguro que desea registrar los datos?")
            #Funcion condicional de confirmacion de registro
            if resultado == "yes":
                registro.append({'nombre': nombre, 'telefono': telefono, 'estado': estado })
                return redirect(url_for('home'))
            else:
                return redirect(url_for('home'))


##################### TIENDA #####################
# Arreglo para almacenar datos
registro1 = []
# 1. Funcion controlador que muestra la tienda
# Definicion de la ruta por defecto,
@app.route('/tienda')
# Lamar a principal
def tienda():
    return render_template('tienda.html',registro1=registro1)

# 2. Funcion controlador para agregar el registro
# Definicion de la ruta
@app.route('/enviar1', methods=['POST'])
# Llamar a enviar
def enviar1():
    # Funcion condicional para enviar los datos del formulario
    if request.method == 'POST':

        nombre = request.form['nombre']
        telefono = request.form['telefono']
        estado = request.form['estado']
        gerente = request.form['gerente']

        # Funcion condicional para no registrar en caso de datos vacios
        if nombre == '' or telefono == '' or estado == '' or gerente == '':
            #Mensaje de alerta de campos faltantes
            messagebox.showwarning("¡Alerta!","Ingrese todos los campos")
            return redirect(url_for('tienda'))

        else:
            #Mensaje de autorizacion de registro
            resultado1 = messagebox.askquestion("Registrar", "¿Está seguro que desea registrar los datos?")
            #Funcion condicional de confirmacion de registro
            if resultado1 == "yes":
                registro1.append({'nombre': nombre, 'telefono': telefono, 'estado': estado, 'gerente': gerente })
                return redirect(url_for('tienda'))
            else:
                return redirect(url_for('tienda'))





# Metodo main del programa
if __name__ == '__main__':
    # debug = True, para reiniciar automatica el servidor
    app.run(debug=True)








