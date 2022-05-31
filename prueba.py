# Importar la biblioteca de flask y librerias necesarias
from tkinter import messagebox
from flask import Flask, redirect, render_template, request, url_for, flash
import pickle

# Instanciar la aplicación
# Nombre por defecto y ruta donde están los modelos
app = Flask(__name__)

# Arreglo para almacenar las tareas
registro = []

# 1. Funcion controlador que muestra la cuenta registrada
# Definicion de la ruta por defecto,
@app.route('/')
# Lamar a principal
def home():
    return render_template('index.html', registro=registro)

# 2. Funcion controlador para registrar cuenta
# Definicion de la ruta
@app.route('/cliente', methods=['POST'])
# Llamar a enviar
def cliente():
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
                registro.append({'nombre': nombre, 'telefono': telefono, 'estado': estado})
                return redirect(url_for('home'))
            else:
                return redirect(url_for('home'))












# Metodo main del programa
if __name__ == '__main__':
    # debug = True, para reiniciar automatica el servidor
    app.run(debug=True)






# 3. Funcion controlador para borrar la lista de tareas
@app.route('/borrar', methods=['POST'])
def borrar():
    if request.method == 'POST':
        # Funcion condicional para mostrar alerta en caso de no existir
        if listaTareas == []:
            messagebox.showwarning("¡Alerta!", "No existen tareas pendientes")
            return redirect(url_for('home'))
        else:
            # Mensaje de autorizacion de borrado
            resultado = messagebox.askquestion(
                "Borrar datos", "¿Está seguro de que desea borrar los datos?")
            # Funcion condicional de confirmacion de borrado
            if resultado == "yes":
                messagebox.showinfo("Info", "Los datos han sido borrados")
                listaTareas.clear()
                return redirect(url_for('home'))
            else:
                return redirect(url_for('home'))

# 4. Funcion controlador para guardar registros en archivo *.pickle
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        # Funcion condicional para mostrar alerta en caso de no existir
        if listaTareas == []:
            messagebox.showwarning(
                "¡Alerta!", "No existen tareas para almacenar")
            return redirect(url_for('home'))
        else:
            # Mensaje de autorizacion de guardado
            resultado = messagebox.askquestion(
                "Guardar registros", "¿Está seguro de que desea guardar los datos?")
            # Funcion condicional de confirmacion de guardado
            if resultado == "yes":
                # Funcion de creacion y sobreescritura de archivo *.pickle
                with open('Tareas.pickle', 'wb') as f:
                    tareas = {'tareas': listaTareas}
                    pickle.dump(tareas, f)
                messagebox.showinfo("Info", "Los datos han sido guardados")
                return redirect(url_for('home'))
            else:
                return redirect(url_for('home'))


# Metodo main del programa
if __name__ == '__main__':
    # debug = True, para reiniciar automatica el servidor
    app.run(debug=True)
