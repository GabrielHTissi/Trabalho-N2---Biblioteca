class StubEmailService:
    def __init__(self):
        self.enviados = []

    def enviar_notificacao_atraso(self, usuario_id: str, mensagem: str):
        self.enviados.append({"usuario_id": usuario_id, "mensagem": mensagem})
