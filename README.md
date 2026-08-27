# Lab Frameworks Back-End — Encontro 3

Repositório de apoio para a aula prática de **introdução ao Flask**, da disciplina Back-End Frameworks (4º Período).

## Objetivos da aula

- Configurar o ambiente Python com `venv` e instalar o Flask.
- Criar sua primeira aplicação web (Hello World).
- Praticar roteamento básico (rotas fixas e dinâmicas).
- Retornar dados em JSON, simulando o início de uma API REST.

## Pré-requisitos

- Python 3.10+ instalado (`python --version` ou `python3 --version` no terminal).
- Um editor de código (recomendado: VS Code).
- Navegador ou Postman/Insomnia para testar as rotas.

## Passo a passo — configurando o ambiente

1. Clone este repositório (ou baixe o ZIP):
   ```bash
   git clone https://github.com/eduhernandes/lab-frameworks-back-end.git
   cd lab-frameworks-back-end
   ```

2. Crie e ative o ambiente virtual:

   **Linux/Mac**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **Windows (PowerShell)**
   ```bash
   python -m venv venv
   venv\Scripts\Activate.ps1
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Rode a aplicação exemplo:
   ```bash
   python app.py
   ```

5. Acesse no navegador: http://127.0.0.1:5000/

## Estrutura do repositório

```
lab-frameworks-back-end/
├── app.py                          # Hello World (Bloco 1)
├── requirements.txt
├── SETUP.md                        # Troubleshooting de erros comuns
├── exemplos/
│   ├── rotas_dinamicas.py          # Bloco 2 - rota /saudacao/<nome> e /api/status
│   └── produtos.py                 # Bloco 2 - lista em memória + rotas GET
├── desafio/
│   ├── enunciado.md                # Bloco 3 - enunciado do desafio TodoList
│   └── todo_app_esqueleto.py       # Bloco 3 - ponto de partida para o desafio
└── README.md
```

> **Deu erro?** Antes de chamar o professor, dá uma olhada no [`SETUP.md`](./SETUP.md) — ele cobre os problemas mais comuns (venv não ativa, porta ocupada, Flask não encontrado, etc).

## Ordem sugerida de estudo (acompanha a aula)

1. `app.py` — primeiro contato com o Flask.
2. `exemplos/rotas_dinamicas.py` — rotas com parâmetros e retorno em JSON.
3. `exemplos/produtos.py` — simulação de um "banco de dados" em memória.
4. `desafio/enunciado.md` + `desafio/todo_app_esqueleto.py` — desafio prático da aula.

## Como entregar o desafio

Depois de resolver o desafio em `desafio/todo_app_esqueleto.py`, gere o arquivo de dependências atualizado e faça commit:

```bash
pip freeze > requirements.txt
git add .
git commit -m "Desafio TodoList resolvido"
git push
```

## Próximo encontro

Protocolo HTTP a fundo (verbos GET, POST, PUT, DELETE, headers, status codes) e como o Flask lida com `request.json` e formulários.
