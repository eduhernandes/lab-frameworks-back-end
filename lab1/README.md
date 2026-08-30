# Lab 1 — Introdução ao Flask

Aula prática de **introdução ao Flask**, da disciplina Back-End Frameworks (4º Período).

> Configuração de ambiente (venv, dependências) está no [README principal](../README.md). Este arquivo cobre só o conteúdo específico deste laboratório.

## Objetivos da aula

- Configurar o ambiente Python com `venv` e instalar o Flask.
- Criar sua primeira aplicação web (Hello World).
- Praticar roteamento básico (rotas fixas e dinâmicas).
- Retornar dados em JSON, simulando o início de uma API REST.

## Como rodar os exemplos

A partir da raiz do repositório, com o ambiente virtual já ativado:

```bash
python lab1/app.py
python lab1/exemplos/rotas_dinamicas.py
python lab1/exemplos/produtos.py
```

Acesse no navegador: http://127.0.0.1:5000/

## Estrutura desta pasta

```
lab1/
├── app.py                          # Hello World (Bloco 1)
├── exemplos/
│   ├── rotas_dinamicas.py          # Bloco 2 - rota /saudacao/<nome> e /api/status
│   └── produtos.py                 # Bloco 2 - lista em memória + rotas GET
└── desafio/
    ├── enunciado.md                # Bloco 3 - enunciado do desafio TodoList
    └── todo_app_esqueleto.py       # Bloco 3 - ponto de partida para o desafio
```

## Ordem sugerida de estudo (acompanha a aula)

1. `app.py` — primeiro contato com o Flask.
2. `exemplos/rotas_dinamicas.py` — rotas com parâmetros e retorno em JSON.
3. `exemplos/produtos.py` — simulação de um "banco de dados" em memória.
4. `desafio/enunciado.md` + `desafio/todo_app_esqueleto.py` — desafio prático da aula.

## Como entregar o desafio

A entrega é feita pelo **Teams**, na aba **Atribuições**, e não pelo GitHub.

1. Depois de resolver o desafio em `lab1/desafio/todo_app_esqueleto.py`, atualize o arquivo de dependências:
   ```bash
   pip freeze > requirements.txt
   ```

2. Compacte a pasta do seu projeto em um único `.zip`. **Não inclua a pasta `venv/`** no arquivo.

3. Nomeie o arquivo obrigatoriamente como:
   ```
   nome_sobrenome_lab1.zip
   ```

4. Envie o `.zip` na atividade correspondente no Teams, dentro do prazo definido em aula.

## Deu erro?

Veja o [`SETUP.md`](../SETUP.md) — cobre os problemas mais comuns (venv não ativa, porta ocupada, Flask não encontrado, etc).

## Próximo laboratório

**Lab 2** — Protocolo HTTP a fundo (verbos GET, POST, PUT, DELETE, headers, status codes) e como o Flask lida com `request.json`.
