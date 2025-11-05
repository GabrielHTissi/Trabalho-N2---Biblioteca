from typing import Dict, List
from models import Livro, Usuario, Emprestimo

class InMemoryLivroRepository:
    def __init__(self):
        self._store: Dict[str, Livro] = {}

    def add(self, livro: Livro):
        self._store[livro.isbn] = livro

    def get(self, isbn: str) -> Livro:
        return self._store[isbn]

class InMemoryUsuarioRepository:
    def __init__(self):
        self._store: Dict[str, Usuario] = {}

    def add(self, u: Usuario):
        self._store[u.id] = u

    def get(self, uid: str) -> Usuario:
        return self._store[uid]

class InMemoryEmprestimoRepository:
    def __init__(self):
        self._store: Dict[str, Emprestimo] = {}

    def add(self, e: Emprestimo):
        self._store[e.id] = e

    def list_by_usuario(self, usuario_id: str) -> List[Emprestimo]:
        return [e for e in self._store.values() if e.usuario_id == usuario_id]

    def get(self, id: str) -> Emprestimo:
        return self._store[id]

    def update(self, e: Emprestimo):
        self._store[e.id] = e
