from unittest import TestCase
from main import mesmo_numero

class TestMesmoNumero(TestCase):
    def test_mesmo_deve_retornar_2_quando_receber_1(self):
        self.assertEqual(mesmo_numero(1), 2)

    def test_mesmo_deve_retornar_3_quando_receber_1(self):
        self.assertEqual(mesmo_numero(1), 3)
