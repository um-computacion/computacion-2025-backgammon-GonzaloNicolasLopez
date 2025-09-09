import unittest
from core.checker import Checker

class TestChecker(unittest.TestCase):
    def test_init(self):
        ficha = Checker("Blancas", 5)
        self.assertEqual(ficha.color, "Blancas")
        self.assertEqual(ficha.posicion, 5)

    def test_mover(self):
        ficha = Checker("Negras", 10)
        ficha.mover(15)
        self.assertEqual(ficha.posicion, 15)

    def test_str_con_posicion(self):
        ficha = Checker("Blancas", 3)
        self.assertEqual(str(ficha), "Ficha Blancas en posición 3")    

if __name__ == "__main__":
    unittest.main()