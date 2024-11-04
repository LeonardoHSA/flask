# imports da biblioteca do flask
from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

# criando um objeto app chamando a função Flask (do tipo Flask),
# o __name__ faz uma referência ao próprio arquivo
app = Flask(__name__)

# a rota da aplicação (127.0.0.1:5000/inicio)
@app.route('/inicio')
# função da rota
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('World of Tanks', 'PVP', 'PC')
    jogo3 = Jogo('War Thunder', 'PVP', 'PC')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='jogos', jogos=lista)

# executando
app.run()
