import time

class MockGatewayPagamento:
    def __init__(self, aprovar: bool = True, delay: float = 0.0):
        self.aprovar = aprovar
        self.delay = delay

    def pagar(self, dados: dict) -> dict:
        if self.delay:
            time.sleep(self.delay)
        return {"status": "aprovado" if self.aprovar else "negado", "id": "txn-123"}
