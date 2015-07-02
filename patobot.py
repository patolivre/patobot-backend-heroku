# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

direcoes_andar = {
    'frente': 1,
    'tras': 2,
}

direcoes_girar = {
    'direita': 3,
    'esquerda': 4,
}


@app.route('/andar/<direcao>')
def andar(direcao):
    return 'PatoBot andou para %s!' % direcao


@app.route('/girar/<direcao>')
def girar(direcao):
    return 'PatoBot girou para %s!' % direcao


@app.route('/')
def main():
    return 'PatoBot :-)'
