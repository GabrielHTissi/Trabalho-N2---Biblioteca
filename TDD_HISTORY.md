# Histórico de Commits (TDD)
Este arquivo descreve os passos e comandos para reproduzir o ciclo **vermelho → verde → refatorar**.

Exemplo de comandos (executar na raiz do projeto `python/`):

1. Inicializar repositório
```
git init
git config user.email "student@example.com"
git config user.name "Aluno Teste"
```

2. Criar um teste que falha (vermelho)
```
# criar tests/test_temp_red.py com um assert False
git add tests/test_temp_red.py
git commit -m "test: adicionar teste que falha (vermelho)"
```

3. Implementar código mínimo para passar o teste (verde)
```
# alterar src/... para adicionar implementação mínima
git add src/
git commit -m "feat: implementação mínima para passar teste (verde)"
```

4. Refatorar sem alterar comportamento (refatorar)
```
# melhorar código, reorganizar funções
git add -A
git commit -m "refactor: limpeza e melhoria"
```

O repositório inclui um script `make_commits.sh` que automatiza este fluxo de demonstração local.
