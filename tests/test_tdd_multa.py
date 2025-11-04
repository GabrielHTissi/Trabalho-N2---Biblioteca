from datetime import datetime, timedelta
import pytest

from src.library_service import MULTA_POR_DIA

def test_calcular_multa_zero_dias(service, tmp_clock):
    previs = tmp_clock.now()
    devol = previs
    assert service.calcular_multa(previs, devol) == 0

def test_calcular_multa_um_dia(service, tmp_clock):
    previs = tmp_clock.now()
    devol = previs + timedelta(days=1)
    assert service.calcular_multa(previs, devol) == MULTA_POR_DIA

# Simule ciclo vermelho -> verde -> refatorar no histórico de commits local (README explica)
