import pytest
from models import Livro
from library_service import LimiteEmprestimoExcedidoError

# (Seu conftest.py já está providenciando a 'service')

def test_limite_emprestimos(service):
    # u1 tem limite 2 (isso está definido no seu setup, provavelmente conftest)
    service.emprestar('e1', 'u1', 'isbn-1')
    service.emprestar('e2', 'u1', 'isbn-2')
    
    # criar um terceiro livro temporário
    # (Removendo o 'from models import Livro' de dentro do teste)
    service.livro_repo.add(Livro(isbn='isbn-3', titulo='Livro 3'))

    # O teste agora espera a exceção CERTA...
    with pytest.raises(LimiteEmprestimoExcedidoError):
        # ...e agora chama a função CORRETAMENTE
        service.emprestar('e3', 'u1', 'isbn-3')

def test_emprestar_livro_indisponivel(service):
    # emprestar isbn-1
    e = service.emprestar('e1', 'u1', 'isbn-1')
    # tentar emprestar novamente o mesmo livro
    with pytest.raises(ValueError):
        service.emprestar('e2', 'u1', 'isbn-1')

