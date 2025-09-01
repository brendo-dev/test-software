import sys
import os
import pytest

# Adiciona o diretório raiz ao path para importar a calculadora
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculadora import Calculadora


class TestCalculadora:
    """Testes para a classe Calculadora."""
    
    def setup_method(self):
        """Configuração executada antes de cada teste."""
        self.calc = Calculadora()
    
    def test_somar(self):
        """Testa a operação de soma."""
        assert self.calc.somar(2, 3) == 5
        assert self.calc.somar(-1, 1) == 0
        assert self.calc.somar(0, 0) == 0
        assert self.calc.somar(-5, -3) == -8
    
    def test_subtrair(self):
        """Testa a operação de subtração."""
        assert self.calc.subtrair(5, 3) == 2
        assert self.calc.subtrair(1, 1) == 0
        assert self.calc.subtrair(0, 5) == -5
        assert self.calc.subtrair(-2, -3) == 1
    
    def test_multiplicar(self):
        """Testa a operação de multiplicação."""
        assert self.calc.multiplicar(3, 4) == 12
        assert self.calc.multiplicar(-2, 3) == -6
        assert self.calc.multiplicar(0, 10) == 0
        assert self.calc.multiplicar(-2, -3) == 6
    
    def test_dividir(self):
        """Testa a operação de divisão."""
        assert self.calc.dividir(10, 2) == 5
        assert self.calc.dividir(9, 3) == 3
        assert self.calc.dividir(-8, 2) == -4
        assert self.calc.dividir(7, 2) == 3.5
    
    def test_dividir_por_zero(self):
        """Testa se a divisão por zero levanta exceção."""
        with pytest.raises(ValueError, match="Divisão por zero não é permitida"):
            self.calc.dividir(10, 0)
    
    def test_potencia(self):
        """Testa a operação de potência."""
        assert self.calc.potencia(2, 3) == 8
        assert self.calc.potencia(5, 2) == 25
        assert self.calc.potencia(10, 0) == 1
        assert self.calc.potencia(2, -2) == 0.25
    
    def test_raiz_quadrada(self):
        """Testa o cálculo da raiz quadrada."""
        assert self.calc.raiz_quadrada(16) == 4
        assert self.calc.raiz_quadrada(25) == 5
        assert self.calc.raiz_quadrada(0) == 0
        assert self.calc.raiz_quadrada(2) == pytest.approx(1.414, abs=0.001)
    
    def test_raiz_quadrada_numero_negativo(self):
        """Testa se a raiz quadrada de número negativo levanta exceção."""
        with pytest.raises(ValueError, match="Não é possível calcular raiz quadrada de número negativo"):
            self.calc.raiz_quadrada(-4)


# Testes parametrizados
class TestCalculadoraParametrizada:
    """Testes parametrizados para a calculadora."""
    
    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (10, -5, 5),
        (100, 200, 300)
    ])
    def test_somar_parametrizado(self, a, b, expected):
        """Testa soma com múltiplos valores."""
        calc = Calculadora()
        assert calc.somar(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (10, 2, 5),
        (20, 4, 5),
        (-10, 2, -5),
        (100, 10, 10)
    ])
    def test_dividir_parametrizado(self, a, b, expected):
        """Testa divisão com múltiplos valores."""
        calc = Calculadora()
        assert calc.dividir(a, b) == expected