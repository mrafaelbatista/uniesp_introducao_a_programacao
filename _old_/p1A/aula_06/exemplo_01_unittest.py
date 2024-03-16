import unittest


def somar(num1, num2):
    return num1 + num2


class TestSomar(unittest.TestCase):

    def test_somar_3_com_5(self):
        self.assertEqual(somar(3, 5), 8)
        
    def test_somar_8_com_75(self):
        self.assertEqual(somar(8, 75), 83)

    def test_somar__1_com__2(self):
        self.assertEqual(somar(-1, -2), -3)


if __name__ == '__main__':
    unittest.main()
