# Desenvolvimento de CI-CD com GitHub Actions ![Test status](https://github.com/LabEngSoftware2025/aula4-calculadora/actions/workflows/python-app.yml/badge.svg) [![python](https://img.shields.io/badge/Python-3.7-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)


Uma aplicação simples de calculadora para a qual vários testes foram criados e configurados para serem executados a cada commit novo do [projeto no repositório GitHub](https://github.com/LabEngSoftware2025/aula4-calculadora)

Criado por:
- Ruan Machado Coelho Rossato
- Rodrigo Galvez Lima
- Gabriel Chaves Lopes Silva


## Testes Implementados

O projeto conta com uma suíte abrangente de testes unitários que verificam o correto funcionamento da calculadora em diversos cenários:

### Testes de Operações Básicas
- **Soma**: Testes com inteiros, decimais e números negativos
- **Subtração**: Verificação de resultados com diferentes tipos numéricos
- **Multiplicação**: Testes com combinações positivas e negativas
- **Divisão**: Operações normais e tratamento de divisão por zero
- **Potenciação**: Testes com bases e expoentes variados

### Testes de Validação de Entrada
- Conversão de strings numéricas para valores
- Tratamento de valores inválidos (strings não numéricas, None)
- Verificação de operações inválidas
- Validação de tipos de dados

### Casos Especiais
- Divisão por zero (retorna None)
- Potenciação com expoente zero
- Números muito grandes e muito pequenos
- Precisão decimal usando `pytest.approx`

## Configuração do CI/CD

O projeto utiliza **GitHub Actions** para implementar um pipeline de integração contínua que executa automaticamente a cada push ou pull request para a branch main.

### Fluxo do Workflow

1. **Checkout do código**: Obtém a versão mais recente do repositório
2. **Configuração do ambiente**: Instala Python 3.10
3. **Instalação de dependências**:
   - `pytest` para execução dos testes
   - `pytest-cov` para análise de cobertura
   - `flake8` para linting do código
4. **Análise de código**:
   - Verificação de erros de sintaxe e problemas críticos
   - Análise de complexidade e estilo de código
5. **Execução dos testes**:
   - Roda toda a suíte de testes
   - Gera relatório de cobertura em formato XML
