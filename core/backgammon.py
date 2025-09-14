from core.board import Board

from core.dice import Dice

from core.player import Player

from core.checker import Checker

class Backgammon:
    def __init__(self, player2, player1):
        self.__jugador1__ = Player(player1, "Negras") 
        self.__jugador2__ = Player(player2, "Blancas")  