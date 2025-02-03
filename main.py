
import dao

from flask import *
app = Flask(__name__)

app.secret_key = 'Khggj3h424j23hg44$#'

@app.route('/logout', methods=['POST', 'GET'])
def sair():
    session.pop('login')
    return render_template('principal.html')

@app.route('/')
def home():
    return render_template('principal.html')

@app.route('/convidado')
def pagina_tabela():
    return render_template('paginag8.html')

@app.route('/verificarlogin', methods=['POST','GET'])
def verificar_login():

    if request.method == 'GET' and 'login' in session:
        return render_template('homepage.html')
    elif request.method == 'GET' and not 'login' in session:
        return render_template('principal.html', msg='Usuário ou senha inválidos')
    elif request.method == 'POST'  and 'login' in session:
        return render_template('homepage.html')
    else:
        login = request.form.get('username')
        senha = request.form.get('password')

        if len(dao.login(login, senha)) > 0:
            session['login'] = login
            return render_template('homepage.html')
        else:
            return render_template('principal.html', msg='Usuário ou senha inválidos')


@app.route('/pagina_cadastro')
def mostrar_pagina_cadastro():
    return render_template('cadastrarusuario.html')


@app.route('/Times', methods=['POST'])
def mostrar_campeao():
    campeao = request.form.get('campeao')
    if dao.mostrar_campeao(campeao, session['login']):
        msg = 'Bom Palpite'
        return render_template('paginag8.html', texto=msg)
    else:
        return redirect(url_for('verificar_login'))



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
    if 'login' in session:

      usuarios = dao.listar_usuarios()
      return render_template('listausuarios.html', lista=usuarios)
    else:
      return render_template('principal.html')

@app.route('/listarvotos')
def listar_votos():
    if 'login' in session:

      campeao = dao.listar_votos()
      return render_template('votos.html', lista=campeao)
    else:
      return render_template('principal.html')

if __name__ == '__main__':
    app.run(debug=True)