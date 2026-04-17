#pip install flask
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mostrarlogin')
def mostrar_pag_login():
    return render_template('paglogin.html')

@app.route('/pagcadastro')
def mostrar_pagcadastro():
    return render_template('cadastro.html')

app.run(debug=True)