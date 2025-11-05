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