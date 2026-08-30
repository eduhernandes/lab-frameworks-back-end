"""
Bloco 3 - Desafio: Mini API de Tarefas (TodoList)

Veja o enunciado completo em desafio/enunciado.md

Como executar:
    python desafio/todo_app_esqueleto.py
"""
from flask import Flask, jsonify

app = Flask(__name__)

# TODO 1: Crie a lista inicial de tarefas em memória.
# Cada tarefa deve ser um dicionário com pelo menos: id, titulo, concluida
tarefas = [
    # Exemplo (pode manter, editar ou apagar):
    # {"id": 1, "titulo": "Estudar Flask", "concluida": False},
]


@app.route('/tarefas')
def listar_tarefas():
    # TODO 2: Retorne todas as tarefas em JSON
    pass


@app.route('/tarefas/<int:id>')
def buscar_tarefa(id):
    # TODO 3: Busque a tarefa pelo id.
    # Se não encontrar, retorne jsonify com erro e status 404.
    pass


@app.route('/sobre')
def sobre():
    # TODO 4: Retorne um JSON com dados da equipe/aluno (nome, turma, etc)
    pass


if __name__ == '__main__':
    app.run(debug=True)
