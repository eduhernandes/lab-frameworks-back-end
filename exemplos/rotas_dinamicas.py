"""
Bloco 2 - Rotas dinâmicas e retorno em JSON

Como executar:
    python exemplos/rotas_dinamicas.py

Rotas disponíveis:
    GET /saudacao/<nome>   -> saudação personalizada
    GET /api/status        -> status do servidor em JSON
"""
from flask import Flask

app = Flask(__name__)


@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo(a) ao Flask."


@app.route('/api/status')
def status():
    # Retornar um dicionário faz o Flask converter automaticamente para JSON
    return {
        "status": "online",
        "servidor": "Flask 3.x",
        "ambiente": "Desenvolvimento"
    }


if __name__ == '__main__':
    app.run(debug=True)
