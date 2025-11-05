# Trabalho N2 — Biblioteca

## Como executar

1. Entrar na pasta `python`.
2. Criar e ativar venv (recomendado).
3. Instalar dependências: `pip install -r requirements.txt`.
4. Rodar testes: `pytest -q`.
5. Gerar cobertura: `coverage run -m pytest && coverage html`.

## Decisões de design
- Repositórios em memória para evitar I/O real.
- `Clock` injetável para facilitar testes determinísticos.
- `StubEmailService` e `MockGatewayPagamento` para dobrar dependências.
- Regras concentradas em `LibraryService` (fácil de testar).

## Mapa de testes
- `test_tdd_multa.py` — TDD do cálculo de multa (exemplos e casos base).
- `test_parametrizado.py` — parametrizados cobrindo dias de atraso.
- `test_excecoes.py` — verifica erros: livro indisponível, limite atingido.
- `test_integration_ponta_a_ponta.py` — fluxo ponta-a-ponta com repositórios em memória.
- `test_performance.py` — teste marcado com `@pytest.mark.slow` medindo tempo.

## Limites conhecidos
- Regras simples: tarifa fixa por dia; não há policy de grace period; não há persistência real.
- Gateway de pagamento é simulado; para testes E2E com pagamento real substituir por adapter.

## INTEGRANTES: 
-GABRIEL TISSI, LUAN FERREIRA DO AMARAL, BRUNO ROVANI MARCELINO, FELIPE DOS SANTOS, BRUNO SCHIMIGUEL, RENAN GABRIEL PIECHONTCOSKI, ERICK ANDREAS PONTICELLI.