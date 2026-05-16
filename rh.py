def calcular_bonus_natal(salario, anos_de_casa, cargo):
    if anos_de_casa > 2 and cargo == 'DESENVOLVEDOR':
        return salario * 0.15
    return 0
