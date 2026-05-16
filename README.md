# Teste de Mutação - Sistema de RH (TechRobot)

**Aluno:** Davi Faita

## O que aprendi

Aprendi na prática que cobertura de código mede apenas se as linhas foram executadas pelos testes, enquanto o Teste de Mutação mede a real qualidade das asserções: um teste fraco pode atingir 100% de cobertura e ainda assim deixar passar mutantes (alterações sutis no código como trocar `>` por `>=` ou `and` por `or`). Só asserções com valores exatos e testes de fronteira matam mutantes de verdade.

## Como executar

```bash
pip install pytest
pytest
```
