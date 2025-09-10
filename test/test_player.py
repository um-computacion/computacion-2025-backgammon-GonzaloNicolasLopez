import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    def test_init(self):
        jugador = Player("Juan", "blanco")
        self.assertEqual(jugador.__nombre__, "Juan")
        self.assertEqual(jugador.__color__, "blanco")

    def test_str(self):
        jugador = Player("Ana", "negro")
        self.assertEqual(str(jugador), "Ana negro")

    def test_tener_nombre(self):
        jugador = Player("Juan", "Blancas")
        self.assertEqual(jugador.tener_nombre(), "Juan")

    def test_tener_color(self):
        jugador = Player("Ana", "Negras")
        self.assertEqual(jugador.tener_color(), "Negras")


if __name__ == "__main__":
    unittest.main()