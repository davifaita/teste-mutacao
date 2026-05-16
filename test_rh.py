from rh import calcular_bonus_natal


def test_desenvolvedor_com_mais_de_2_anos_recebe_15_porcento():
    assert calcular_bonus_natal(5000, 5, 'DESENVOLVEDOR') == 750.0


def test_desenvolvedor_com_exatos_2_anos_nao_recebe_bonus():
    assert calcular_bonus_natal(5000, 2, 'DESENVOLVEDOR') == 0


def test_desenvolvedor_com_1_ano_nao_recebe_bonus():
    assert calcular_bonus_natal(5000, 1, 'DESENVOLVEDOR') == 0


def test_analista_com_mais_de_2_anos_nao_recebe_bonus():
    assert calcular_bonus_natal(5000, 5, 'ANALISTA') == 0


def test_gerente_com_10_anos_nao_recebe_bonus():
    assert calcular_bonus_natal(8000, 10, 'GERENTE') == 0


def test_desenvolvedor_com_3_anos_fronteira_recebe_bonus():
    assert calcular_bonus_natal(4000, 3, 'DESENVOLVEDOR') == 600.0


def test_cargo_em_minusculo_nao_recebe_bonus():
    assert calcular_bonus_natal(5000, 5, 'desenvolvedor') == 0
