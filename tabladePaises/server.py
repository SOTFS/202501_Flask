

from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def tabla_de_paises():
    return render_template('index.html', paises=paises)
paises = [

   {'pais': 'Argentina' , 'capital': 'Buenos Aires'},

   {'pais': 'Brasil' , 'capital': 'Brasilia'},

   {'pais': 'Chile' , 'capital': 'Santiago de Chile'},

   {'pais': 'Colombia' , 'capital': 'Bogotá'},

   {'pais': 'Costa Rica' , 'capital': 'San José'},

   {'pais': 'Paraguay' , 'capital': 'Asunción'},

   {'pais': 'Perú' , 'capital': 'Lima'}

]


if __name__ == '__main__':
    app.run(debug=True)
    