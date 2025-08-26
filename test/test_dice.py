
import unittest
from core.dice import Dice

class TestDice(unittest.TestCase):
    def test_tirar_dado(self):
        dado = Dice()
        dado.tirar()
        self.assertTrue(all(1 <= x <= 6 for x in dado.__movimiento__))


        
if __name__ == "__main__":
    unittest.main()