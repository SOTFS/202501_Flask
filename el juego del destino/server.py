from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'clavesuperpro'

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    session['nombre'] = request.form['nombre']
    session['numero'] = request.form['numero']
    session['lugar'] = request.form['ciudad']
    session['favorita'] = request.form['comida']
    session['profesion'] = request.form['profesion']
    return redirect(url_for('futuro'))

@app.route('/futuro')
def futuro():
    mensaje = random.choice([True, False])
    return render_template('futuro.html', mensaje=mensaje)
if __name__ == '__main__':

    app.run(debug=True)