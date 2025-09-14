import unittest
from core.backgammon import Backgammon
from core.player import Player

class TestBackgammon(unittest.TestCase):
    def test_init(self):
        juego = Backgammon("Gonzalo", "Pedro")
        self.assertIsInstance(juego.__jugador1__, Player)
        self.assertIsInstance(juego.__jugador2__, Player)
        self.assertEqual(juego.__jugador1__.tener_nombre(), "Pedro")
        self.assertEqual(juego.__jugador1__.tener_color(), "Negras")
        self.assertEqual(juego.__jugador2__.tener_nombre(), "Gonzalo")
        self.assertEqual(juego.__jugador2__.tener_color(), "Blancas")

if __name__ == "__main__":
    unittest.main()