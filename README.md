# Teste de Mutação - Sistema de RH (TechRobot)

**Aluno:** Davi Faita

## Sobre o projeto

Atividade prática da disciplina de QA Test (UniSENAI - Prof. MSc. Hugo Menezes Barra) que demonstra como 100% de cobertura de código não garante a ausência de bugs. O sistema calcula o bônus de Natal (15% sobre o salário) para desenvolvedores com mais de 2 anos de casa.

## O que aprendi

Aprendi na prática que cobertura de código mede apenas se as linhas foram executadas pelos testes, enquanto o Teste de Mutação mede a real qualidade das asserções: um teste fraco pode atingir 100% de cobertura e ainda assim deixar passar mutantes (alterações sutis no código como trocar `>` por `>=` ou `and` por `or`). Só asserções com valores exatos e testes de fronteira matam mutantes de verdade.

## Como executar

```bash
pip install pytest
pytest
```
