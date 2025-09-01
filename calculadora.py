class Calculadora:
    """
    Uma calculadora simples para operações matemáticas básicas.
    """
    
    def somar(self, a, b):
        """Soma dois números."""
        return a + b
    
    def subtrair(self, a, b):
        """Subtrai o segundo número do primeiro."""
        return a - b
    
    def multiplicar(self, a, b):
        """Multiplica dois números."""
        return a * b
    
    def dividir(self, a, b):
        """Divide o primeiro número pelo segundo."""
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b
    
    def potencia(self, base, expoente):
        """Calcula base elevado ao expoente."""
        return base ** expoente
    
    def raiz_quadrada(self, numero):
        """Calcula a raiz quadrada de um número."""
        if numero < 0:
            raise ValueError("Não é possível calcular raiz quadrada de número negativo")
        return numero ** 0.5


def main():
    calc = Calculadora()
    
    print("=== Calculadora Simples ===")
    print(f"2 + 3 = {calc.somar(2, 3)}")
    print(f"10 - 5 = {calc.subtrair(10, 5)}")
    print(f"4 * 6 = {calc.multiplicar(4, 6)}")
    print(f"15 / 3 = {calc.dividir(15, 3)}")
    print(f"2^3 = {calc.potencia(2, 3)}")
    print(f"√16 = {calc.raiz_quadrada(16)}")


if __name__ == "__main__":
    main()