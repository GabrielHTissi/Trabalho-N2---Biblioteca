import pytest
# IMPORTANDO DATETIME PARA CRIAR DATAS FALSAS
from datetime import datetime, timedelta 

from library_service import LibraryService, LimiteEmprestimoExcedidoError
from models import Usuario, Livro, Emprestimo
from repository import InMemoryLivroRepository, InMemoryUsuarioRepository, InMemoryEmprestimoRepository
from clock import Clock
from gateway import EmailGateway 

# --- INÍCIO DO TESTE ---

def test_usuario_nao_pode_pegar_mais_de_3_livros():
    # 1. Setup (Cenário) - COM AS DEPENDÊNCIAS
    livro_repo = InMemoryLivroRepository()
    usuario_repo = InMemoryUsuarioRepository()
    emprestimo_repo = InMemoryEmprestimoRepository()
    clock = Clock()
    email_service = EmailGateway() 

    servico = LibraryService(
        livro_repo=livro_repo,
        usuario_repo=usuario_repo,
        emprestimo_repo=emprestimo_repo,
        clock=clock,
        email_service=email_service
    )
    
    # Criando o cenário
    usuario = Usuario(id="user1", nome="Teste", limite_emprestimos=3)
    usuario_repo.add(usuario) # Usando .add()
    
    livro1 = Livro(isbn="111", titulo="Livro 1", disponivel=False)
    livro2 = Livro(isbn="222", titulo="Livro 2", disponivel=False)
    livro3 = Livro(isbn="333", titulo="Livro 3", disponivel=False)
    livro4 = Livro(isbn="444", titulo="Livro 4", disponivel=True)
    
    livro_repo.add(livro1) # Usando .add()
    livro_repo.add(livro2) # Usando .add()
    livro_repo.add(livro3) # Usando .add()
    livro_repo.add(livro4) # Usando .add()

    # Simula que o usuário já tem 3 livros (usando Emprestimos)
    
    # CRIANDO DATAS FALSAS PARA O CONSTRUTOR
    data_fake_inicio = datetime(2025, 1, 1)
    data_fake_prevista = datetime(2025, 1, 8)

    # CORRIGINDO O CONSTRUTOR DO EMPRESTIMO E USANDO .add()
    emprestimo_repo.add(Emprestimo(id="e1", usuario_id="user1", isbn="111", data_inicio=data_fake_inicio, data_prevista_devolucao=data_fake_prevista))
    emprestimo_repo.add(Emprestimo(id="e2", usuario_id="user1", isbn="222", data_inicio=data_fake_inicio, data_prevista_devolucao=data_fake_prevista))
    emprestimo_repo.add(Emprestimo(id="e3", usuario_id="user1", isbn="333", data_inicio=data_fake_inicio, data_prevista_devolucao=data_fake_prevista))


    # 2. Ação (Tentar pegar o 4º livro)
    with pytest.raises(LimiteEmprestimoExcedidoError):
        servico.emprestar(emprestimo_id="e4", usuario_id="user1", isbn="444")