from datetime import timedelta
from typing import List
from models import Emprestimo, Livro, Usuario

MULTA_POR_DIA = 1.5  # R$ por dia de atraso (exemplo)
PRAZO_PADRAO_DIAS = 7

class LibraryService:
    def __init__(self, livro_repo, usuario_repo, emprestimo_repo, clock, email_service):
        self.livro_repo = livro_repo
        self.usuario_repo = usuario_repo
        self.emprestimo_repo = emprestimo_repo
        self.clock = clock
        self.email = email_service

    def emprestar(self, emprestimo_id: str, usuario_id: str, isbn: str):
        usuario = self.usuario_repo.get(usuario_id)
        livro = self.livro_repo.get(isbn)

        # regras: livro disponivel
        if not livro.disponivel:
            raise ValueError("Livro não disponível")

        ativos = [e for e in self.emprestimo_repo.list_by_usuario(usuario_id) if e.data_devolucao is None]
        if len(ativos) >= usuario.limite_emprestimos:
            raise ValueError("Limite de empréstimos atingido")

        agora = self.clock.now()
        previsto = agora + timedelta(days=PRAZO_PADRAO_DIAS)
        e = Emprestimo(id=emprestimo_id, usuario_id=usuario_id, isbn=isbn, data_inicio=agora, data_prevista_devolucao=previsto)
        livro.disponivel = False
        self.livro_repo.add(livro)
        self.emprestimo_repo.add(e)
        return e

    def devolver(self, emprestimo_id: str):
        agora = self.clock.now()
        e = self.emprestimo_repo.get(emprestimo_id)
        if e.data_devolucao is not None:
            raise ValueError("Empréstimo já devolvido")
        e.data_devolucao = agora
        dias = e.dias_atraso(agora)
        multa = dias * MULTA_POR_DIA
        e.multa_pago = multa
        self.emprestimo_repo.update(e)

        livro = self.livro_repo.get(e.isbn)
        livro.disponivel = True
        self.livro_repo.add(livro)

        if dias > 0:
            self.email.enviar_notificacao_atraso(e.usuario_id, f"Você tem {dias} dias de atraso. Multa: R$ {multa:.2f}")

        return e

    def calcular_multa(self, data_prevista, data_devolucao) -> float:
        dias = (data_devolucao.date() - data_prevista.date()).days
        return max(0, dias) * MULTA_POR_DIA

def test_usuario_nao_pode_pegar_mais_de_3_livros():
    # 1. Setup (Cenário)
    servico = LibraryService() # (ou o nome da sua classe de serviço)
    usuario = Usuario(nome="Teste")

    # Simula que o usuário já tem 3 livros
    servico.emprestar_livro(usuario, Livro(titulo="Livro 1"))
    servico.emprestar_livro(usuario, Livro(titulo="Livro 2"))
    servico.emprestar_livro(usuario, Livro(titulo="Livro 3"))

    # 2. Ação (Tentar pegar o 4º livro)
    # O teste espera que isso levante uma exceção
    with pytest.raises(LimiteEmprestimoExcedidoError): # Um erro que você vai criar
        servico.emprestar_livro(usuario, Livro(titulo="Livro 4"))