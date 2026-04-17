#pip install flask
from flask import *
from usuario import Usuario

app = Flask(__name__)

lista_usuarios = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mostrarlogin', methods=['GET'])
def mostrar_pag_login():
    return render_template('paglogin.html')

@app.route('/pagcadastro')
def mostrar_pagcadastro():
    return render_template('cadastro.html')

#se deixar o método sem nada ele considera como GET
@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    nome = request.form.get('nome')
    login = request.form.get('login')
    senha = request.form.get('senha')
    confirma = request.form.get('confirma')
    tipo = request.form.get('tipo')
    print(nome,login,senha,confirma,tipo)
    if senha == confirma:
        #instanciar um objeto da classe Usuario
        novo_usuario = Usuario(nome, login, senha, tipo)
        lista_usuarios.append(novo_usuario)
        texto='Usuário cadastrado com sucesso!'
        return render_template('cadastro.html' , msg=texto)
    else:
        texto = 'Erro no cadastro. Verifique sua senha!'
        return render_template('cadastro.html', msg=texto)



app.run(debug=True)