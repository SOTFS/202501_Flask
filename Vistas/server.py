from flask import Flask, session, redirect, url_for, render_template, request

app = Flask(__name__)
app.secret_key = 'clave'

@app.route('/')
def index():
    # Inicializar visitas y reinicios si no existen en la sesión
    if 'contador' in session:
        session['contador'] += 1
    else:
        session['contador'] = 0

    if 'reinicios' not in session:
        session['reinicios'] = 0
    
    
    return render_template('home.html', contador=session['contador'], reinicios=session['reinicios'])

@app.route('/destruir_sesion', methods=['GET', 'POST'])
def destruir_sesion():
    session.clear()  
    return redirect(url_for('sesion'))

@app.route('/sesion')
def sesion():
    return render_template('index.html')

@app.route('/sumar_dos')
def sumar_dos():
    session['contador'] += 1 # al recargar la pagina se suma por defecto 1
    return redirect(url_for('index'))

@app.route('/reiniciar')
def reiniciar():
    session['contador'] = 0
    session['reinicios'] += 1
    return redirect(url_for('index'))

@app.route('/aumentar', methods=['POST'])
def aumentar():
    cantidad = int(request.form.get('numero', 0))
    session['contador'] += cantidad -1 # al recargar la pagina se suma por defecto 1

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)