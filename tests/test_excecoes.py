import pytest

def test_emprestar_livro_indisponivel(service):
    # emprestar isbn-1
    e = service.emprestar('e1', 'u1', 'isbn-1')
    # tentar emprestar novamente o mesmo livro
    with pytest.raises(ValueError):
        service.emprestar('e2', 'u1', 'isbn-1')

def test_limite_emprestimos(service):
    # u1 tem limite 2
    service.emprestar('e1', 'u1', 'isbn-1')
    service.emprestar('e2', 'u1', 'isbn-2')
    # criar um terceiro livro temporário
    from src.models import Livro
    service.livro_repo.add(Livro(isbn='isbn-3', titulo='Livro 3'))
    with pytest.raises(ValueError):
        service.emprestar('e3', 'u1', 'isbn-3')
