import unittest

def somar(a, b):
    return a + b

class TestSoma(unittest.TestCase):

    def test_soma_positivos(self):
        self.assertEqual(somar(2, 3), 7)

    def test_soma_negativos(self):
        self.assertEqual(somar(-1, -1), -2)


if __name__ == '__main__':
    unittest.main()
