
import unittest
from unittest.mock import patch
from core.dice import Dice


class TestDice(unittest.TestCase):
    def test_tirar_dado(self):
        dado = Dice()
        dado.tirar()
        self.assertTrue(all(1 <= x <= 6 for x in dado.__movimiento__))

    @patch('random.randint', side_effect=[5, 2])
    def test_tirada_simple(self, mock_randint):
        dado = Dice()
        dado.tirar()
        mov = dado.obtener_movimiento()
        self.assertEqual(len(mov), 2)
        self.assertEqual(mov[0], 5)
        self.assertEqual(mov[1], 2)
        self.assertTrue(mock_randint.called)
        self.assertEqual(mock_randint.call_count, 2)

    @patch('random.randint', return_value=1)
    def test_tirada_doble(self, mock_randint):
        dado = Dice()
        dado.tirar()
        mov = dado.obtener_movimiento()
        self.assertEqual(len(mov), 4)
        self.assertEqual(mov, [1, 1, 1, 1])
        self.assertTrue(mock_randint.called)
        self.assertEqual(mock_randint.call_count, 2)

    @patch('random.randint', side_effect=Exception("error!!"))
    def test_error_en_randint(self, mock_randint):
        dado = Dice()
        try:
            dado.tirar()
        except Exception as e:
            self.assertEqual(str(e), "error!!")
        self.assertTrue(mock_randint.called)
        self.assertEqual(mock_randint.call_count, 1) 
        
if __name__ == "__main__":
    unittest.main()