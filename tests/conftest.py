import pytest
from datetime import datetime, timedelta
from repository import InMemoryLivroRepository, InMemoryUsuarioRepository, InMemoryEmprestimoRepository
from clock import StubClock
from email import StubEmailService
from gateway import MockGatewayPagamento
from library_service import LibraryService
from models import Livro, Usuario

@pytest.fixture
def tmp_clock():
    return StubClock(datetime(2025, 1, 1, 10, 0, 0))

@pytest.fixture
def repos():
    l = InMemoryLivroRepository()
    u = InMemoryUsuarioRepository()
    e = InMemoryEmprestimoRepository()
    return l, u, e

@pytest.fixture
def service(repos, tmp_clock):
    livro_repo, usuario_repo, emprestimo_repo = repos
    email = StubEmailService()
    gateway = MockGatewayPagamento(aprovar=True, delay=0)
    svc = LibraryService(livro_repo, usuario_repo, emprestimo_repo, tmp_clock, email)
    # preparar dados básicos
    usuario_repo.add(Usuario(id='u1', nome='Alice', limite_emprestimos=2))
    livro_repo.add(Livro(isbn='isbn-1', titulo='Livro 1'))
    livro_repo.add(Livro(isbn='isbn-2', titulo='Livro 2'))
    return svc
