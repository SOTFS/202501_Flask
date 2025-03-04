from flask import Flask, render_template, request, redirect, session #Agregamos request y redirect

app = Flask(__name__)

# La ruta raíz renderizará nuestro formulario

@app.route('/')

def index():

   return render_template("index.html")

# /crear_usuario recibe la información

# /crear_usuario recibe la información

@app.route('/crear_usuario', methods=['POST'])

def crear_usuario():

   print("Recibiendo información")

   print(request.form)

   #Creamos dos propiedades de sesión y almacenamos el nombre e email recibido del formulario

   session['nombre_usuario'] = request.form['nombre']

   session['email_usuario'] = request.form['email']

   return redirect('/mostrar_usuario')
@app.route('/mostrar_usuario')

def mostrar_usuario():

   print("Usuario redirigido")

   print(session['nombre_usuario'])

   print(session['email_usuario'])

   return render_template("mostrar.html")

if __name__ == "__main__":

   app.run(debug=True)