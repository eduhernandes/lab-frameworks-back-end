# Desafio — Mini API de Tarefas (TodoList)

**Tempo sugerido:** 40 minutos
**Formato:** individual ou em duplas
**Arquivo de trabalho:** `desafio/todo_app_esqueleto.py`

## O que fazer

Complete o arquivo `todo_app_esqueleto.py` para que ele atenda aos requisitos abaixo. Os pontos que precisam ser preenchidos estão marcados com `# TODO`.

1. **Lista inicial de tarefas em memória**
   Crie uma lista de dicionários, cada um representando uma tarefa, com pelo menos os campos `id`, `titulo` e `concluida`.

2. **Rota `GET /tarefas`**
   Deve retornar todas as tarefas cadastradas, em formato JSON.

3. **Rota `GET /tarefas/<int:id>`**
   Deve retornar os detalhes de uma única tarefa pelo `id`.
   Se o `id` não existir, retornar erro 404 com uma mensagem clara.

4. **Rota `GET /sobre`**
   Deve retornar um JSON com informações da equipe/aluno responsável (nome, turma, etc).

## Como testar

Com o servidor rodando (`python desafio/todo_app_esqueleto.py`), acesse no navegador ou no Postman:

- http://127.0.0.1:5000/tarefas
- http://127.0.0.1:5000/tarefas/1
- http://127.0.0.1:5000/sobre

## Critérios de conclusão

- [ ] As 4 rotas funcionam sem erros.
- [ ] Buscar uma tarefa inexistente retorna status 404.
- [ ] O código está organizado e comentado.
- [ ] `requirements.txt` atualizado com `pip freeze > requirements.txt`.

## Desafio extra (opcional)

Se sobrar tempo, tente:
- Adicionar um campo `prioridade` (baixa, media, alta) nas tarefas.
- Criar uma rota `GET /tarefas/pendentes` que retorna só as tarefas com `concluida: false`.
