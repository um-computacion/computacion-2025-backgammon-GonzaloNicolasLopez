import unittest
from core.board import Board

class TestBoard(unittest.TestCase):

    def test_sin_ficha(self):
        board = Board()
        self.assertEqual(board.__contenedor__[1], [])
        self.assertEqual(board.__contenedor__[2], [])
        self.assertEqual(board.__contenedor__[3], [])
        self.assertEqual(board.__contenedor__[4], [])
        self.assertEqual(board.__contenedor__[6], [])
        self.assertEqual(board.__contenedor__[8], [])
        self.assertEqual(board.__contenedor__[9], [])
        self.assertEqual(board.__contenedor__[10], [])
        self.assertEqual(board.__contenedor__[13], [])
        self.assertEqual(board.__contenedor__[14], [])
        self.assertEqual(board.__contenedor__[15], [])
        self.assertEqual(board.__contenedor__[17], [])
        self.assertEqual(board.__contenedor__[19], [])
        self.assertEqual(board.__contenedor__[20], [])
        self.assertEqual(board.__contenedor__[21], [])
        self.assertEqual(board.__contenedor__[22], [])

    def test_con_ficha(self):
        board = Board()
        self.assertEqual(board.__contenedor__[0], ["Negras"]*2)
        self.assertEqual(board.__contenedor__[11], ["Negras"]*5)
        self.assertEqual(board.__contenedor__[16], ["Negras"]*3)
        self.assertEqual(board.__contenedor__[18], ["Negras"]*5)
        self.assertEqual(board.__contenedor__[5], ["Blancas"]*5)
        self.assertEqual(board.__contenedor__[7], ["Blancas"]*3)
        self.assertEqual(board.__contenedor__[12], ["Blancas"]*5)
        self.assertEqual(board.__contenedor__[23], ["Blancas"]*2)

if __name__ == "__main__":
     unittest.main()