from unittest import TestCase
from exemplo_01_funcoes import multiplicar
from exemplo_01_funcoes import dividir

class TestMultiplicar(TestCase):

    def test_multiplicar_dois_por_tres(self):
        self.assertEqual(multiplicar(2, 3), 6)

    def test_multiplicar_quatro_por_dez(self):
        self.assertEqual(multiplicar(4, 10), 40)

class TestDividir(TestCase):

    def test_dividir_10_por_2(self):
        self.assertEqual(dividir(10, 2), 5)

