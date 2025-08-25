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

if __name__ == "__main__":
    unittest.main()