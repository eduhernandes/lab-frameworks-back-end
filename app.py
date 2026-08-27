"""
Bloco 1 - Primeiro servidor Flask (Hello World)

Como executar:
    python app.py

Depois acesse: http://127.0.0.1:5000/
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Minha primeira aplicação Back-End com Flask!"


if __name__ == '__main__':
    app.run(debug=True)
