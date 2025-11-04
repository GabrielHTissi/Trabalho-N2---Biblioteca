import pytest
from datetime import timedelta

@pytest.mark.parametrize(
    "dias_atraso, esperado",
    [
        (0, 0.0),
        (1, 1.5),
        (5, 7.5),
    ],
)
def test_param_calculo_multa(service, tmp_clock, dias_atraso, esperado):
    previs = tmp_clock.now()
    devol = previs + timedelta(days=dias_atraso)
    assert service.calcular_multa(previs, devol) == pytest.approx(esperado)
