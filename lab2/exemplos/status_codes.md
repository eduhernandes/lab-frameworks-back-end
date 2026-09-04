# Referência rápida — Status Codes

Cola de consulta para usar durante o laboratório. Não é exaustiva — cobre os
códigos usados nos exemplos e no desafio desta aula.

## 2xx — Sucesso

| Código | Nome | Quando usar |
|---|---|---|
| 200 | OK | Sucesso genérico (GET, PUT, DELETE com corpo de resposta) |
| 201 | Created | Um novo recurso foi criado (resposta de um POST) |
| 204 | No Content | Sucesso, mas sem corpo de resposta (comum em DELETE) |

## 4xx — Erro do cliente

| Código | Nome | Quando usar |
|---|---|---|
| 400 | Bad Request | O corpo da requisição está ausente ou mal formado |
| 401 | Unauthorized | Faltou se autenticar (ex: header Authorization ausente) |
| 403 | Forbidden | Autenticado, mas sem permissão para aquela ação |
| 404 | Not Found | O recurso solicitado não existe (ex: tarefa com id inexistente) |
| 415 | Unsupported Media Type | Content-Type errado ou ausente no corpo enviado |

## 5xx — Erro do servidor

| Código | Nome | Quando usar |
|---|---|---|
| 500 | Internal Server Error | Uma exceção não tratada aconteceu no código do servidor |

## Regra prática

- **2xx**: "deu certo".
- **4xx**: "o cliente pediu algo errado" (a culpa é de quem fez a requisição).
- **5xx**: "o servidor quebrou" (a culpa é do código do back-end).
