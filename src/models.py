from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional

@dataclass
class Livro:
    isbn: str
    titulo: str
    disponivel: bool = True

@dataclass
class Usuario:
    id: str
    nome: str
    limite_emprestimos: int = 3

@dataclass
class Emprestimo:
    id: str
    usuario_id: str
    isbn: str
    data_inicio: datetime
    data_prevista_devolucao: datetime
    data_devolucao: Optional[datetime] = None
    multa_pago: float = 0.0

    def esta_atrasado(self, agora: datetime) -> bool:
        if self.data_devolucao:
            return self.data_devolucao > self.data_prevista_devolucao
        return agora > self.data_prevista_devolucao

    def dias_atraso(self, agora: datetime) -> int:
        fim = self.data_devolucao or agora
        delta = (fim.date() - self.data_prevista_devolucao.date()).days
        return max(0, delta)
