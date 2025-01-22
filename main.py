
import dao

from flask import *
app = Flask(__name__)

@app.route('/login' , methods=['POST'])
def fazer_login():
    login = request.form.get('username')
    senha = request.form.get('password')

    if len(dao.login(login, senha)) > 0:
        return render_template('homepage.html')
    else:
         return render_template('principal.html')



@app.route('/')
def home():
    return render_template('principal.html')

@app.route('/convidado')
def pagina_tabela():
    return render_template('paginag8.html')

@app.route('/verificarlogin', methods=['POST'])
def verificar_login():
    login = request.form.get('username')
    senha = request.form.get('password')

    if len(dao.login(login, senha)) > 0:
        return render_template('homepage.html')
    else:
        return render_template('principal.html', msg='Usuário ou senha inválidos')


@app.route('/pagina_cadastro')
def mostrar_pagina_cadastro():
    return render_template('cadastrarusuario.html')

@app.route('/cadastrarusuario', methods=['POST'])
def cadastrar_usuario():
    nome = request.form.get('nome')
    login = request.form.get('login')
    senha = request.form.get('senha')

    if dao.inserir_user(nome, login, senha):
        msg = 'usuario inserido com sucesso'
        return render_template('principal.html', texto=msg)

@app.route('/listausuarios')
def listar_usuarios():

    usuarios = dao.listar_usuarios()
    print(usuarios)
    return render_template('listausuarios.html', lista=usuarios)


if __name__ == '__main__':
    app.run(debug=True)