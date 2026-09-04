"""
Lab 2 - Desafio: Mini API de Tarefas com CRUD completo

Veja o enunciado completo em lab2/desafio/enunciado.md

Como executar:
    python lab2/desafio/todo_app_crud_esqueleto.py
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Estudar Flask", "concluida": False},
    {"id": 2, "titulo": "Revisar o desafio anterior", "concluida": True},
]
proximo_id = 3


@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas), 200


@app.route('/tarefas/<int:id>', methods=['GET'])
def buscar_tarefa(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)
    if tarefa is None:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    return jsonify(tarefa), 200


@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    global proximo_id
    # TODO 1: valide o Content-Type (request.is_json) e retorne 415 se faltar
    # TODO 2: leia o corpo com request.get_json()
    # TODO 3: se não vier "titulo", retorne 400 com uma mensagem de erro
    # TODO 4: crie a nova tarefa, adicione em `tarefas`, incremente proximo_id
    # TODO 5: retorne a tarefa criada com status 201
    pass


@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    # TODO 1: busque a tarefa pelo id; se não existir, retorne 404
    # TODO 2: valide o Content-Type e retorne 415 se faltar
    # TODO 3: leia o corpo e atualize os campos da tarefa
    # TODO 4: retorne a tarefa atualizada com status 200
    pass


@app.route('/tarefas/<int:id>', methods=['DELETE'])
def remover_tarefa(id):
    global tarefas
    # TODO 1: busque a tarefa pelo id; se não existir, retorne 404
    # TODO 2: remova a tarefa da lista `tarefas`
    # TODO 3: retorne uma resposta vazia com status 204
    pass


if __name__ == '__main__':
    app.run(debug=True)
