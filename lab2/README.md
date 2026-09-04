# Lab 2 — Protocolo HTTP no Back-End

Continuação do lab-frameworks-back-end. Nesta aula, a API de tarefas criada
no **Lab 1** ganha o ciclo completo de CRUD (Create, Read, Update, Delete),
usando verbos HTTP, headers, corpo em JSON e códigos de status.

## Pré-requisito

Ambiente já configurado no Lab 1 (`venv` + Flask instalado). Se for uma
máquina nova, siga o [README principal](../README.md) primeiro.

## Como rodar os exemplos

A partir da raiz do repositório, com o ambiente virtual já ativado:

```bash
python lab2/exemplos/verbos_http.py
python lab2/exemplos/headers_status.py
```

## Como testar rotas POST / PUT / DELETE

O navegador não envia facilmente requisições com corpo JSON. Use uma destas opções:

- **curl** (já vem instalado no terminal, sem precisar instalar nada extra) — os comandos exatos estão em cada arquivo de exemplo e no `desafio/enunciado.md`.
- **Postman** ou **Insomnia**, se já estiverem instalados no laboratório.
- **Thunder Client** (extensão do VS Code), se preferir não sair do editor.

## Estrutura desta pasta

```
lab2/
├── exemplos/
│   ├── verbos_http.py           # GET, POST, PUT, DELETE sobre o recurso de tarefas
│   ├── headers_status.py        # Headers customizados, Content-Type, Authorization
│   └── status_codes.md          # Cola de consulta rápida dos códigos usados na aula
└── desafio/
    ├── enunciado.md             # Enunciado: evoluir a API para CRUD completo
    └── todo_app_crud_esqueleto.py  # Ponto de partida do desafio
```

## Ordem sugerida de estudo

1. `exemplos/verbos_http.py` — rode e teste cada verbo com os comandos `curl` do topo do arquivo.
2. `exemplos/headers_status.py` — rode e observe os headers/status nas respostas (`curl -i`).
3. `exemplos/status_codes.md` — use como referência enquanto resolve o desafio.
4. `desafio/enunciado.md` + `desafio/todo_app_crud_esqueleto.py` — desafio prático da aula.

## Como entregar o desafio

Mesmo fluxo do Lab 1: `.zip` do projeto pela aba **Atribuições** do Teams,
nomeado como:

```
nome_sobrenome_lab2.zip
```

Detalhes completos no `desafio/enunciado.md`.

## Deu erro?

Veja o [`SETUP.md`](../SETUP.md) — inclui uma seção específica de
troubleshooting de `curl` e requisições HTTP.
