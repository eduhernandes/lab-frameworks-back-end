# SETUP.md — Guia de Solução de Problemas

Este guia cobre os erros mais comuns que costumam travar quem está configurando o ambiente pela primeira vez no laboratório. Leia o item que corresponde à sua mensagem de erro.

---

## 1. "python não é reconhecido como comando" / "command not found: python"

**Causa:** Python não está instalado ou não está no PATH do sistema.

**Solução:**
- No Windows, tente `py` no lugar de `python`:
  ```bash
  py -m venv venv
  ```
- No Linux/Mac, tente `python3` no lugar de `python`:
  ```bash
  python3 -m venv venv
  ```
- Se nada funcionar, confirme a instalação com `python --version` (ou `python3 --version`, ou `py --version`). Se nenhum retornar versão, o Python precisa ser instalado (avise o professor/monitor).

---

## 2. Erro ao ativar o venv no Windows (PowerShell): "não pode ser carregado porque a execução de scripts foi desabilitada"

**Causa:** Política de execução do PowerShell bloqueia scripts `.ps1`.

**Solução (uma das opções):**
- Rode este comando uma única vez nesse terminal e tente ativar de novo:
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  venv\Scripts\Activate.ps1
  ```
- Ou use o Prompt de Comando (cmd) em vez do PowerShell:
  ```cmd
  venv\Scripts\activate.bat
  ```

---

## 3. Terminal não mostra `(venv)` no início da linha

**Causa:** O ambiente virtual não foi ativado (ou foi ativado em outro terminal).

**Solução:**
- Confirme que você está na pasta do projeto (`lab-frameworks-back-end`).
- Rode o comando de ativação de novo:
  - Linux/Mac: `source venv/bin/activate`
  - Windows PowerShell: `venv\Scripts\Activate.ps1`
  - Windows cmd: `venv\Scripts\activate.bat`
- Se fechou o terminal, é normal precisar ativar de novo a cada nova sessão — o venv não fica "sempre ativo".

---

## 4. "ModuleNotFoundError: No module named 'flask'"

**Causa:** O Flask não foi instalado, ou foi instalado fora do venv ativo.

**Solução:**
1. Confirme que o venv está ativado (veja o item 3).
2. Instale novamente:
   ```bash
   pip install -r requirements.txt
   ```
3. Se ainda der erro, confira se o `pip` usado é o do venv:
   ```bash
   pip --version
   ```
   O caminho mostrado deve conter `venv` na pasta. Se não conter, o venv não está ativo.

---

## 5. "Address already in use" / "OSError: [Errno 98] Address already in use" / porta 5000 ocupada

**Causa:** Já existe outro processo (às vezes uma execução anterior do Flask) usando a porta 5000. É comum em Mac, onde o AirPlay Receiver também usa a porta 5000.

**Solução:**
- Opção rápida — rode em outra porta:
  ```python
  app.run(debug=True, port=5001)
  ```
  E acesse `http://127.0.0.1:5001/`.
- Ou feche o processo antigo:
  - Linux/Mac: `lsof -i :5000` para achar o PID, depois `kill -9 <PID>`.
  - Windows: `netstat -ano | findstr :5000` para achar o PID, depois `taskkill /PID <PID> /F`.
- No Mac, também é possível desativar o AirPlay Receiver em Ajustes > Geral > AirDrop e Handoff.

---

## 6. Página abre mas mostra "This site can't be reached" ou não carrega

**Causa:** O servidor não está rodando, travou, ou a URL está errada.

**Solução:**
- Confira no terminal se apareceu a mensagem `Running on http://127.0.0.1:5000`. Se não apareceu, o servidor não iniciou — veja se há erro de sintaxe no `app.py` acima dessa linha.
- Use exatamente a URL mostrada no terminal (a porta pode variar se você mudou no código).
- Tente `http://localhost:5000/` como alternativa a `127.0.0.1`.

---

## 7. Alterei o código mas o navegador continua mostrando a versão antiga

**Causa:** O servidor não está em modo debug, ou o navegador está com cache.

**Solução:**
- Confirme que o `app.run()` está com `debug=True` — nesse modo o Flask recarrega sozinho ao salvar o arquivo.
- Se mesmo assim não atualizar, pare o servidor (`Ctrl+C` no terminal) e rode de novo.
- Force o recarregamento no navegador com `Ctrl+F5` (ou `Cmd+Shift+R` no Mac).

---

## 8. "TemplateNotFound" ou erros relacionados a `templates/`

**Causa:** Esse erro não deveria aparecer nos exemplos deste laboratório (não usamos templates HTML ainda), mas pode surgir se algum aluno tentar usar `render_template` por conta própria.

**Solução:**
- Nesta aula, todas as rotas retornam texto simples ou JSON (dicionários Python), sem necessidade de arquivos de template. Isso será visto em um encontro futuro.

---

## 9. Erro 404 ao acessar uma rota que "deveria existir"

**Causa:** Erro de digitação na URL, barra final divergente, ou o arquivo rodando não é o esperado.

**Solução:**
- Confira se a rota no código bate exatamente com a URL digitada (maiúsculas/minúsculas importam).
- Confirme qual arquivo está rodando no terminal — é comum o aluno editar `exemplos/produtos.py` mas continuar rodando `app.py` em outro terminal aberto.

---

## 10. Erro 500 (Internal Server Error) ao acessar uma rota

**Causa:** Exceção não tratada no código Python daquela rota.

**Solução:**
- Com `debug=True`, o próprio navegador mostra o traceback do erro — leia a última linha, que geralmente indica a causa (ex: `KeyError`, `TypeError`).
- Revise a rota indicada no traceback linha por linha.

---

## 11. `curl: command not found` (Windows)

**Causa:** Versões antigas do Windows não têm `curl` no PowerShell/cmd por padrão (Windows 10 1803+ já vem com ele).

**Solução:**
- Confirme a versão: `curl --version`. Se não existir, use o **Git Bash** (instalado junto com o Git) — ele sempre tem `curl`.
- Alternativa: usar Postman ou Insomnia com interface gráfica em vez do terminal.

---

## 12. Erro 415 "Unsupported Media Type" ao enviar POST/PUT

**Causa:** Esqueceu de enviar o header `Content-Type: application/json`, ou o Flask não reconheceu o corpo como JSON.

**Solução:**
- Confirme que o comando `curl` inclui `-H "Content-Type: application/json"`.
- No Postman/Insomnia, confira a aba **Headers** ou selecione o tipo de corpo como **JSON** na aba **Body**.

---

## 13. Erro 400 "Bad Request" ou corpo chega como `None` no `request.get_json()`

**Causa:** O JSON enviado está mal formatado (aspas simples em vez de duplas, vírgula sobrando, chaves não fechadas).

**Solução:**
- JSON exige aspas duplas: `{"titulo": "Estudar"}`, nunca `{'titulo': 'Estudar'}`.
- No terminal (Windows/PowerShell), aspas simples ao redor do JSON podem causar problemas de escape — prefira Git Bash ou copie o comando exatamente como está no enunciado.
- Valide o JSON em um validador online se não tiver certeza da formatação.

---

## 14. `curl` não mostra nada, ou trava sem resposta

**Causa:** O servidor Flask não está rodando, ou está rodando em outra porta.

**Solução:**
- Confirme que o `python app.py` (ou o arquivo do exemplo/desafio) está rodando em outro terminal.
- Adicione `-i` ao comando `curl` para ver os headers de resposta e confirmar se a requisição chegou.
- Se estiver usando outra porta (ex: 5001), ajuste a URL no comando `curl` de acordo.

---

## Checklist rápido antes de pedir ajuda ao professor

- [ ] O venv está ativado (aparece `(venv)` no terminal)?
- [ ] Rodei `pip install -r requirements.txt` dentro do venv?
- [ ] O terminal mostra `Running on http://127.0.0.1:5000`?
- [ ] Estou acessando a URL exatamente como aparece no terminal?
- [ ] Salvei o arquivo antes de testar no navegador?

Se todos os itens acima estiverem OK e o problema persistir, chame o professor/monitor com a mensagem de erro completa em mãos — copiar o erro do terminal agiliza muito o diagnóstico.
