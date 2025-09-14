import unittest
from core.backgammon import Backgammon
from core.player import Player
from core.board import Board

class TestBackgammon(unittest.TestCase):
    def test_init(self):
        juego = Backgammon("Gonzalo", "Pedro")
        self.assertIsInstance(juego.__jugador1__, Player)
        self.assertIsInstance(juego.__jugador2__, Player)
        self.assertEqual(juego.__jugador1__.tener_nombre(), "Pedro")
        self.assertEqual(juego.__jugador1__.tener_color(), "Negras")
        self.assertEqual(juego.__jugador2__.tener_nombre(), "Gonzalo")
        self.assertEqual(juego.__jugador2__.tener_color(), "Blancas")


    def test_jugador1(self):
        self.game = Backgammon("Gonzalo", "Pedro")
        jugador1 = self.game.jugador1()
        self.assertIsInstance(jugador1, Player)
        self.assertEqual(jugador1.tener_nombre(), "Pedro")
        self.assertEqual(jugador1.tener_color(), "Negras")

    def test_jugador2(self):
        self.game = Backgammon("Gonzalo", "Pedro")
        jugador2 = self.game.jugador2()
        self.assertIsInstance(jugador2, Player)
        self.assertEqual(jugador2.tener_nombre(), "Gonzalo")
        self.assertEqual(jugador2.tener_color(), "Blancas")

    def test_tablero(self):
        self.game = Backgammon("Gonzalo", "Pedro")
        tablero = self.game.tablero()
        self.assertIsInstance(tablero, Board)


if __name__ == "__main__":
    unittest.main()