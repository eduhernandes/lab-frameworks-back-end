"""
Lab 2 - Bloco 2: Headers e Status Codes

Como executar:
    python lab2/exemplos/headers_status.py

Como testar:
    # Ver os headers da resposta (curl -i inclui os headers na saída)
    curl -i http://127.0.0.1:5000/ping

    # Rota que só aceita JSON com Content-Type correto
    curl -i -X POST http://127.0.0.1:5000/echo \
         -H "Content-Type: application/json" \
         -d '{"mensagem": "oi"}'

    # Mesma rota, sem o header Content-Type (veja o erro 415)
    curl -i -X POST http://127.0.0.1:5000/echo -d '{"mensagem": "oi"}'

    # Rota que simula autenticação via header customizado
    curl -i http://127.0.0.1:5000/perfil -H "Authorization: Bearer token123"
    curl -i http://127.0.0.1:5000/perfil
"""
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)


@app.route('/ping')
def ping():
    resposta = make_response(jsonify({"mensagem": "pong"}))
    # Header customizado - qualquer informação extra sobre a resposta
    resposta.headers['X-Powered-By'] = 'Turma-Backend-4periodo'
    return resposta, 200


@app.route('/echo', methods=['POST'])
def echo():
    # request.is_json verifica o header Content-Type enviado pelo cliente
    if not request.is_json:
        return jsonify({"erro": "Envie o header Content-Type: application/json"}), 415

    dados = request.get_json()
    return jsonify({"voce_enviou": dados}), 200


@app.route('/perfil')
def perfil():
    auth = request.headers.get('Authorization')

    if auth is None:
        # 401 Unauthorized: faltou se identificar
        return jsonify({"erro": "Header Authorization ausente"}), 401

    return jsonify({"usuario": "convidado", "token_recebido": auth}), 200


if __name__ == '__main__':
    app.run(debug=True)
