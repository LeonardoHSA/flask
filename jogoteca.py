# imports da biblioteca do flask
from flask import Flask, render_template, request, redirect, session, flash


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('World of Tanks', 'PVP', 'PC')
jogo3 = Jogo('War Thunder', 'PVP', 'PC')
lista = [jogo1, jogo2, jogo3]

# criando um objeto app chamando a função Flask (do tipo Flask),
# o __name__ faz uma referência ao próprio arquivo
app = Flask(__name__)
# chave de criptografia
app.secret_key = 'alura'


# a rota da aplicação (127.0.0.1:5000/)
@app.route('/')
# função da rota
def index():
    return render_template('lista.html', titulo='jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


# Rota para a tela de login
@app.route('/login')
def login():
    return render_template('login.html')

# Rota para autenticar usuário
@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'batata' == request.form['senha']:
        # session para manter dados no cookies do navegador
        session['usuario_logado'] = request.form['usuario']
        # mensagem para ser exibida para o usuário
        flash(session['usuario_logado'] + ' logado com sucesso')
        return redirect('/')
    else:
        flash('Usuário não logado.')
        return redirect('/login')


# executando em modo debug
app.run(debug=True)
