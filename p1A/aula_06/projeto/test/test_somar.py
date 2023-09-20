import unittest
from ..calculadora import somar


class TestSomar(unittest.TestCase):

    def test_somar_5_com_5(self):
        self.assertEqual(somar(5, 5), 10)


if __name__ == '__main__':
    unittest.main()