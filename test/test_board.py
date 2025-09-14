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


    def test_mover_ficha_fuera_de_rango(self):
        board = Board()
        resultado = board.mover_ficha(-1, 5, "Blancas")
        self.assertFalse(resultado)
        resultado = board.mover_ficha(5, 24, "Blancas")
        self.assertFalse(resultado)

    def test_mover_ficha_color_incorrecto(self):
        board = Board()
        resultado = board.mover_ficha(0, 1, "Blancas")
        self.assertFalse(resultado)

    def test_mover_ficha_sin_fichas(self):
        board = Board()
        resultado =board.mover_ficha(2, 3, "Blancas")
        self.assertFalse(resultado)


    def test_comer_ficha(self):
        self.board = Board()
        self.board.__contenedor__[4] = ["Negras"]
        self.board.reserva() 
        resultado = self.board.comer_ficha(4, "Blancas")
        self.assertEqual(self.board.__contenedor__[4], ["Blancas"])
        self.assertEqual(self.board.__reserva__["Negras"], 1)
        self.assertFalse(resultado) 

    def test_no_hay_fichas(self):
        self.board = Board()
        for i in range(24):
            self.board.__contenedor__[i] = [f for f in self.board.__contenedor__[i] if f != "Blancas"]
        self.assertTrue(self.board.no_hay_fichas("Blancas"))
        self.assertFalse(self.board.no_hay_fichas("Negras")) 

    def test_reserva(self):
        self.board = Board()
        reserva = self.board.reserva()
        self.assertEqual(reserva, {"Negras": 0, "Blancas": 0})
        self.board.__reserva__["Negras"] += 1
        self.assertEqual(self.board.__reserva__["Negras"], 1)

    def test_get_contenedor(self):
        self.board = Board()
        contenedor = self.board.get_contenedor()
        self.assertIsInstance(contenedor, list)
        self.assertEqual(len(contenedor), 24)
        self.assertEqual(contenedor[0], ["Negras"]*2)

    def test_comer_ficha_vacio(self):
        self.board = Board()
        self.board.__contenedor__[5] = []
        resultado = self.board.comer_ficha(5, "Blancas")
        self.assertFalse(resultado)

    def test_comer_muchas_fichas(self):
        self.board = Board()
        self.board.__contenedor__[6] = ["Negras", "Negras"]
        resultado = self.board.comer_ficha(6, "Blancas")
        self.assertFalse(resultado)

if __name__ == "__main__":
     unittest.main()