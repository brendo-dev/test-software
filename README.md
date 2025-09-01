# Calculadora Python com CI

Um projeto Python simples demonstrando uma calculadora com testes automatizados usando GitHub Actions.

## Estrutura do Projeto

```
projeto/
├── .github/
│   └── workflows/
│       └── ci.yml
├── test/
│   └── test_calculadora.py
├── calculadora.py
├── requirements.txt
└── README.md
```

## Funcionalidades

A calculadora possui as seguintes operações:
- ✅ Soma
- ✅ Subtração
- ✅ Multiplicação
- ✅ Divisão (com tratamento de divisão por zero)
- ✅ Potenciação
- ✅ Raiz quadrada (com tratamento de números negativos)

## Como usar

### Executar a calculadora:
```bash
python calculadora.py
```

### Instalar dependências:
```bash
pip install -r requirements.txt
```

### Executar testes:
```bash
pytest test/
```

### Executar testes com mais detalhes:
```bash
pytest test/ -v
```

### Executar testes com cobertura:
```bash
pytest test/ --cov=calculadora
```

## CI/CD

O projeto inclui um workflow do GitHub Actions que:
- ✅ Executa em push e pull requests para a branch `main`
- ✅ Usa Python 3.10
- ✅ Instala dependências automaticamente
- ✅ Executa todos os testes com pytest
- ✅ Pode ser executado manualmente via `workflow_dispatch`

## Testes

Os testes cobrem:
- Operações matemáticas básicas
- Casos extremos (divisão por zero, raiz de número negativo)
- Testes parametrizados para múltiplas entradas
- Tratamento de exceções

Total de testes: **15 testes**

## Como contribuir

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

Os testes serão executados automaticamente via GitHub Actions!