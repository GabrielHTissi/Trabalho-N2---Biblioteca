def test_fluxo_completo(service, tmp_clock):
    # 1) criar emprestimo
    e = service.emprestar('e1', 'u1', 'isbn-1')
    assert not service.livro_repo.get('isbn-1').disponivel

    # 2) avançar o relógio para gerar atraso
    tmp_clock.shift_days(3)

    # 3) devolver (gera multa)
    e2 = service.devolver('e1')
    assert e2.multa_pago == service.calcular_multa(e2.data_prevista_devolucao, e2.data_devolucao)

    # 4) email enviado se atraso
    if e2.dias_atraso(tmp_clock.now()) > 0:
        assert service.email.enviados

    # 5) estado final do livro
    assert service.livro_repo.get('isbn-1').disponivel
