"""
Bloco 2 - Simulação de cadastro simples (dados em memória)

Como executar:
    python exemplos/produtos.py

Rotas disponíveis:
    GET /produtos              -> lista todos os produtos
    GET /produtos/<produto_id> -> busca um produto pelo id
"""
from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500.00},
    {"id": 2, "nome": "Mouse", "preco": 45.90},
    {"id": 3, "nome": "Teclado", "preco": 120.00},
]


@app.route('/produtos')
def listar_produtos():
    return jsonify(produtos)


@app.route('/produtos/<int:produto_id>')
def buscar_produto(produto_id):
    produto = next((p for p in produtos if p["id"] == produto_id), None)
    if produto is None:
        return jsonify({"erro": "Produto não encontrado"}), 404
    return jsonify(produto)


if __name__ == '__main__':
    app.run(debug=True)
