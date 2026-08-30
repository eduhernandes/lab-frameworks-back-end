# Lab Frameworks Back-End

Repositório de apoio para as aulas práticas da disciplina **Back-End Frameworks**
(4º Período). Cada laboratório evolui a mesma API de tarefas, construída em Flask.

| Pasta | Conteúdo |
|---|---|
| [`lab1/`](./lab1) | Introdução ao Flask — venv, rotas, JSON, primeira API |
| [`lab2/`](./lab2) | Protocolo HTTP a fundo — verbos, headers, body, status codes |

## Pré-requisitos

- Python 3.10+ instalado (`python --version` ou `python3 --version` no terminal).
- Um editor de código (recomendado: VS Code).
- Navegador ou Postman/Insomnia/curl para testar as rotas.

## Passo a passo — configurando o ambiente

Esse setup é feito **uma única vez** e vale para todos os laboratórios do repositório.

1. Clone este repositório (ou baixe o ZIP):
   ```bash
   git clone https://github.com/SEU-USUARIO/lab-frameworks-back-end.git
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

4. Confirme que está tudo certo rodando o exemplo do Lab 1:
   ```bash
   python lab1/app.py
   ```
   Acesse http://127.0.0.1:5000/ — se aparecer uma mensagem de boas-vindas, o ambiente está pronto.

## Estrutura do repositório

```
lab-frameworks-back-end/
├── README.md                       # este arquivo — índice geral
├── SETUP.md                        # troubleshooting de erros comuns (venv, porta, curl, etc)
├── requirements.txt
├── lab1/                           # Laboratório 1 — Introdução ao Flask
│   ├── README.md
│   ├── app.py
│   ├── exemplos/
│   └── desafio/
├── lab2/                           # Laboratório 2 — Protocolo HTTP a fundo
│   ├── README.md
│   ├── exemplos/
│   └── desafio/
└── correcao/                       # Scripts de correção em lote (uso do professor)
    ├── smoke_test_lab1.py
    └── smoke_test_lab2.py
```

Cada pasta `labN/` tem seu próprio `README.md` com objetivos, ordem de estudo e
instruções de entrega específicas daquele laboratório.

## Deu erro?

Antes de chamar o professor, dá uma olhada no [`SETUP.md`](./SETUP.md) — ele
cobre os problemas mais comuns (venv não ativa, porta ocupada, Flask não
encontrado, erro 415 no curl, etc).

## Como entregar os desafios

Todos os laboratórios seguem o mesmo fluxo: `.zip` do projeto enviado pela aba
**Atribuições** do Teams, nomeado como `nome_sobrenome_labN.zip` (ex:
`joao_silva_lab1.zip`). Detalhes específicos de cada desafio estão no
`README.md` e no `desafio/enunciado.md` de cada pasta `labN/`.
