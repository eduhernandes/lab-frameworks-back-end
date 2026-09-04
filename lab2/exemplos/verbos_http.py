"""
Lab 2 - Bloco 1: Verbos HTTP (GET, POST, PUT, DELETE)

Evolui a API de tarefas do Lab 1 para suportar o ciclo completo de CRUD
(Create, Read, Update, Delete), usando o corpo da requisição (request.json)
para receber dados do cliente.

Como executar:
    python lab2/exemplos/verbos_http.py

Como testar (não dá para testar POST/PUT/DELETE só pelo navegador):

    # GET - listar
    curl http://127.0.0.1:5000/tarefas

    # POST - criar
    curl -X POST http://127.0.0.1:5000/tarefas \
         -H "Content-Type: application/json" \
         -d '{"titulo": "Estudar para a prova"}'

    # PUT - atualizar
    curl -X PUT http://127.0.0.1:5000/tarefas/1 \
         -H "Content-Type: application/json" \
         -d '{"titulo": "Estudar Flask", "concluida": true}'

    # DELETE - remover
    curl -X DELETE http://127.0.0.1:5000/tarefas/1
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
    dados = request.get_json(silent=True)

    if not dados or "titulo" not in dados:
        return jsonify({"erro": "Campo 'titulo' é obrigatório"}), 400

    nova_tarefa = {
        "id": proximo_id,
        "titulo": dados["titulo"],
        "concluida": dados.get("concluida", False),
    }
    tarefas.append(nova_tarefa)
    proximo_id += 1

    # 201 Created: convenção para indicar que um novo recurso foi criado
    return jsonify(nova_tarefa), 201


@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)
    if tarefa is None:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    dados = request.get_json(silent=True)
    if not dados:
        return jsonify({"erro": "Corpo da requisição precisa ser um JSON válido"}), 400

    tarefa["titulo"] = dados.get("titulo", tarefa["titulo"])
    tarefa["concluida"] = dados.get("concluida", tarefa["concluida"])

    return jsonify(tarefa), 200


@app.route('/tarefas/<int:id>', methods=['DELETE'])
def remover_tarefa(id):
    global tarefas
    tarefa = next((t for t in tarefas if t["id"] == id), None)
    if tarefa is None:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    tarefas = [t for t in tarefas if t["id"] != id]

    # 204 No Content: sucesso, mas não há corpo para retornar
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
