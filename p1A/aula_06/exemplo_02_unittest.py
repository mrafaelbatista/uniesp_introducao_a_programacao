import unittest

def aprovado(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        return 1
    else:
        return 0

class TestAprovado(unittest.TestCase):

    def test_aprovado_com_7(self):
        self.assertEqual(aprovado(7, 7, 7), 1)

    def test_reprovado_com_5(self):
        self.assertEqual(aprovado(5, 5, 5,), 0)

if __name__ == '__main__':
    unittest.main()