import time

class MockGatewayPagamento:
    def __init__(self, aprovar: bool = True, delay: float = 0.0):
        self.aprovar = aprovar
        self.delay = delay

    def pagar(self, dados: dict) -> dict:
        if self.delay:
            time.sleep(self.delay)
        return {"status": "aprovado" if self.aprovar else "negado", "id": "txn-123"}

# Este é o conteúdo de 'src/gateway.py'

class EmailGateway:
    
    def enviar_notificacao_atraso(self, usuario_id, mensagem):
        # Na vida real, isso se conectaria com um serviço de email.
        # Por enquanto, podemos só "fingir" que funciona.
        print(f"[Email Falso] Enviando para {usuario_id}: {mensagem}")
        pass