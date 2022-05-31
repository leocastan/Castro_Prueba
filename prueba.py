# Importar la biblioteca de flask y librerias necesarias
from tkinter import messagebox
from flask import Flask, redirect, render_template, request, url_for, flash
import pickle

# Instanciar la aplicación
# Nombre por defecto y ruta donde están los modelos
app = Flask(__name__)

# Arreglo para almacenar las tareas
registro = []

# 1. Funcion controlador que muestra lista actual de tareas pendientes y un formulario para ingresar un nuevo elemento
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

# Metodo main del programa
if __name__ == '__main__':
    # debug = True, para reiniciar automatica el servidor
    app.run(debug=True)








