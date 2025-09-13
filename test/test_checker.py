import unittest
from core.checker import Checker

class TestChecker(unittest.TestCase):
    def test_init(self):
        pieza = Checker("Blancas", 5)
        self.assertEqual(pieza.color, "Blancas")
        self.assertEqual(pieza.posicion, 5)

    def test_mover(self):
        pieza = Checker("Negras", 10)
        pieza.mover(15)
        self.assertEqual(pieza.posicion, 15)

    def test_str_con_posicion(self):
        pieza = Checker("Blancas", 3)
        self.assertEqual(str(pieza), "Ficha Blancas en posición 3")   

    def test_pieza(self):
        pieza = Checker("Blancas", 8)
        self.assertEqual(pieza.pieza(), "Blancas")
        pieza2 = Checker("Negras")
        self.assertEqual(pieza2.pieza(), "Negras")

    def test_contenedor_con_posicion(self):
        pieza = Checker("Blancas", 5)
        self.assertEqual(pieza.contenedor(), 5)

    def test_contenedor_sin_posicion(self):
        pieza = Checker("Negras")
        self.assertIsNone(pieza.contenedor())     

if __name__ == "__main__":
    unittest.main()