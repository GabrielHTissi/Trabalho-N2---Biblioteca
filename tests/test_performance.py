import time
import pytest

@pytest.mark.slow
def test_deve_ser_rapido(service):
    t0 = time.perf_counter()
    # operação simples: emprestar + devolver
    e = service.emprestar('ep', 'u1', 'isbn-2')
    service.devolver('ep')
    assert (time.perf_counter() - t0) < 0.5
