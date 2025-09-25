import pytest
from calculadora import calculadora


class TestCalculadora:

    # Testes do Comportamento Esperado
    def test_soma_inteiros(self):
        assert calculadora(5, 3, '+') == 8.0
    
    def test_soma_decimais(self):
        assert calculadora(2.5, 1.5, '+') == 4.0

    def test_soma_negativos(self):
        assert calculadora(-5, -2.5, '+') == -7.5


    
    def test_subtracao_inteiros(self):
        assert calculadora(10, 4, '-') == 6.0
    
    def test_subtracao_decimais(self):
        assert calculadora(5.5, 2.2, '-') == pytest.approx(3.3)
        
    def test_subtracao_negativos(self):
        assert calculadora(-5, -1.5, '-') == -3.5


    
    def test_multiplicacao_inteiros(self):
        assert calculadora(4, 3, '*') == 12.0
    
    def test_multiplicacao_decimais(self):
        assert calculadora(2.5, 4.0, '*') == 10.0

    def test_multiplicacao_negativo(self):
        assert calculadora(2.5, -4.0, '*') == -10.0


    
    def test_divisao_inteiros(self):
        assert calculadora(10, 2, '/') == 5.0
    
    def test_divisao_decimais(self):
        assert calculadora(7.5, 2.5, '/') == 3.0

    def test_divisao_negativo(self):
        assert calculadora(7.5, -2.5, '/') == -3.0


    
    def test_potenciacao_inteiros(self):
        assert calculadora(2, 3, '^') == 8.0
    
    def test_potenciacao_decimais(self):
        assert calculadora(4.0, 0.5, '^') == 2.0

    def test_potenciacao_negativos(self):
        assert calculadora(-4.0, 3., '^') == -64.0
    


    # Testes de casos especiais
    def test_divisao_por_zero(self):
        assert calculadora(10, 0, '/') is None
    
    def test_potencia_zero(self):
        assert calculadora(5, 0, '^') == 1.0
    
    def test_potencia_base_zero(self):
        assert calculadora(0, 5, '^') == 0.0
    


    # Testes com strings que podem ser convertidas
    def test_valores_string_numerica(self):
        assert calculadora("10", "2", '+') == 12.0
    
    def test_valores_string_decimais(self):
        assert calculadora("3.14", "1.86", '+') == 5.0
    

    # Testes de validação de entrada
    def test_operacao_invalida(self):
        assert calculadora(5, 3, '%') is None
    
    def test_valor1_invalido(self):
        assert calculadora("abc", 3, '+') is None
    
    def test_valor2_invalido(self):
        assert calculadora(5, "xyz", '+') is None
    
    def test_ambos_valores_invalidos(self):
        assert calculadora("abc", "xyz", '+') is None
    
    # Teste de tipo None
    def test_valor_none(self):
        assert calculadora(None, 5, '+') is None


    # Teste de performance/edge cases
    def test_numeros_muito_grandes(self):
        resultado = calculadora(1e100, 1e100, '*')
        assert resultado == 1e200

    def test_numeros_muito_pequenos(self):
        resultado = calculadora(1e-100, 1e-100, '*')
        assert resultado == 1e-200