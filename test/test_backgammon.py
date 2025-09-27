import unittest
from core.backgammon import Backgammon
from core.player import Player
from core.board import Board
from unittest.mock import patch

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
        game = Backgammon("Gonzalo", "Pedro")
        jugador1 = game.jugador1()
        self.assertIsInstance(jugador1, Player)
        self.assertEqual(jugador1.tener_nombre(), "Pedro")
        self.assertEqual(jugador1.tener_color(), "Negras")

    def test_jugador2(self):
        game = Backgammon("Gonzalo", "Pedro")
        jugador2 = game.jugador2()
        self.assertIsInstance(jugador2, Player)
        self.assertEqual(jugador2.tener_nombre(), "Gonzalo")
        self.assertEqual(jugador2.tener_color(), "Blancas")

    def test_tablero(self):
        game = Backgammon("Gonzalo", "Pedro")
        tablero = game.tablero()
        self.assertIsInstance(tablero, Board)

    def test_tirar_dados(self):
        game = Backgammon("Gonzalo", "Pedro")
        game.dados_tirados()
        self.assertTrue(game.dados_tirados(),all(1 <= x <= 6 for x in game.dados_tirados()))

    def test_turno(self):
        game = Backgammon("Gonzalo", "Pedro")
        turno = game.turno()
        self.assertIsInstance(turno, Player)
        self.assertEqual(turno.tener_nombre(), "Pedro")
        self.assertEqual(turno.tener_color(), "Negras")
        
    def test_get_dados(self):
        game = Backgammon("Gonzalo", "Pedro")
        game.dados_tirados() 
        self.assertTrue(game.get_dados(),all(1 <= x <= 6 for x in game.dados_tirados())) 

    def test_especificar_turno(self):
        game = Backgammon("Gonzalo", "Pedro")
        self.assertEqual(game.turno().tener_nombre(), "Pedro")
        game.especificar_turno()
        self.assertEqual(game.turno().tener_nombre(), "Gonzalo") 
        game.especificar_turno()
        self.assertEqual(game.turno().tener_nombre(), "Pedro")

if __name__ == "__main__":
    unittest.main()