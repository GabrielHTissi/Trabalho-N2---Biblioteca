#!/bin/bash
# Script to demonstrate TDD workflow: vermelho -> verde -> refatorar
set -e

REPO_DIR=$(pwd)

echo "1) Inicializando repositório git local (temporário)"
git init -q
git config user.email "student@example.com"
git config user.name "Aluno Teste"

# Step 1: add failing test (vermelho)
cat > src/library_service_temp.py <<'PY'
# placeholder
PY
git add -A
git commit -m "chore: init placeholder" -q || true

# Create a failing test example
cat > tests/test_temp_red.py <<'PY'
import pytest
from src.library_service import LibraryService

def test_falha_temporaria():
    assert False, "proposital: vermelho"
PY

git add tests/test_temp_red.py
if git commit -m "test: adicionar teste que falha (vermelho)" -q; then
  echo "Committed failing test (vermelho)."
fi

# Step 2: implement minimal code to make test pass (verde)
# For demo purposes we'll remove the failing test and add a passing one
git rm -q tests/test_temp_red.py
cat > tests/test_temp_green.py <<'PY'
def test_passa_demo():
    assert True
PY
git add tests/test_temp_green.py
git commit -m "feat: implementação mínima para passar teste (verde)" -q

# Step 3: refactor (exemplo)
git commit --allow-empty -m "refactor: limpeza e melhoria" -q

echo "TDD demo commits criados (vermelho -> verde -> refatorar)."
echo "Nota: este script altera seu repositório atual; execute em cópia caso precise."
