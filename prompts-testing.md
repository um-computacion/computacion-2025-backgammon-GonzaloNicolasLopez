CHAT GPT -4.1

dame un test de la clase player 

import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    def test_init(self):
        jugador = Player("Juan", "blanco")
        self.assertEqual(jugador._Player__nombre__, "Juan")
        self.assertEqual(jugador._Player__color__, "blanco")

if __name__ == "__main__":
    unittest.main()

dame un test de la clase board  de test_contenedor

import unittest
from core.board import Board

 def test_get_contenedor(self):
        contenedor = self.board.get_contenedor()
        self.assertIsInstance(contenedor, list)
        self.assertEqual(len(contenedor), 24)
        self.assertEqual(contenedor[0], ["Negras"]*2)

if __name__ == "__main__":
    unittest.main()

Implemente estos testeos adaptandolos a mi codigo
