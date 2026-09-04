# Desafio — Mini API de Tarefas, agora com CRUD completo

**Tempo sugerido:** 60 minutos
**Formato:** individual ou em duplas
**Arquivo de trabalho:** `lab2/desafio/todo_app_crud_esqueleto.py`
**Pré-requisito:** desafio do Lab 1 (esse arquivo já parte de uma versão pronta com GET)

## Contexto

No Lab 1, sua API só sabia **ler** tarefas (GET). Agora ela vai aprender a
**criar, atualizar e remover** tarefas também — o CRUD completo de um recurso.

## O que fazer

Complete os pontos marcados com `# TODO` no arquivo esqueleto:

1. **`POST /tarefas`** — cria uma nova tarefa a partir do corpo JSON enviado.
   - Campo obrigatório: `titulo`.
   - Se `titulo` não vier no corpo, retornar **400** com uma mensagem de erro.
   - Se criar com sucesso, retornar a tarefa criada com status **201**.

2. **`PUT /tarefas/<int:id>`** — atualiza uma tarefa existente.
   - Se o `id` não existir, retornar **404**.
   - Se existir, atualizar os campos enviados e retornar a tarefa atualizada com **200**.

3. **`DELETE /tarefas/<int:id>`** — remove uma tarefa existente.
   - Se o `id` não existir, retornar **404**.
   - Se remover com sucesso, retornar **204** (sem corpo).

4. **Validação de Content-Type** — as rotas `POST` e `PUT` devem retornar **415**
   se o cliente não enviar o header `Content-Type: application/json`.

## Como testar

Use os comandos `curl` abaixo (não dá para testar POST/PUT/DELETE só no navegador):

```bash
# Listar (já deve funcionar, herdado do Lab 1)
curl http://127.0.0.1:5000/tarefas

# Criar
curl -X POST http://127.0.0.1:5000/tarefas \
     -H "Content-Type: application/json" \
     -d '{"titulo": "Nova tarefa"}'

# Atualizar
curl -X PUT http://127.0.0.1:5000/tarefas/1 \
     -H "Content-Type: application/json" \
     -d '{"concluida": true}'

# Remover
curl -X DELETE http://127.0.0.1:5000/tarefas/1

# Conferir os códigos de status retornados (adicione -i em qualquer comando acima)
curl -i http://127.0.0.1:5000/tarefas/999
```

Se preferir uma interface visual em vez do terminal, qualquer um destes
funciona igual: Postman, Insomnia ou a extensão Thunder Client do VS Code.

## Critérios de conclusão

- [ ] `POST /tarefas` cria a tarefa e retorna 201
- [ ] `POST /tarefas` sem `titulo` retorna 400
- [ ] `PUT /tarefas/<id>` atualiza e retorna 200
- [ ] `PUT /tarefas/<id>` com id inexistente retorna 404
- [ ] `DELETE /tarefas/<id>` remove e retorna 204
- [ ] `DELETE /tarefas/<id>` com id inexistente retorna 404
- [ ] Rotas POST/PUT sem `Content-Type: application/json` retornam 415
- [ ] `requirements.txt` atualizado com `pip freeze > requirements.txt`

## Desafio extra (opcional)

- Adicione uma rota `PATCH /tarefas/<id>/concluir` que marca uma tarefa como concluída
  sem precisar enviar o objeto inteiro.
- Adicione validação: `titulo` não pode ser uma string vazia.
