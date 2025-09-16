from core.board import Board

from core.dice import Dice

from core.player import Player

from core.checker import Checker

class Backgammon:
   
    def __init__(self, player2, player1):
        self.__jugador1__ = Player(player1, "Negras") 
        self.__jugador2__ = Player(player2, "Blancas")  
        self.__tablero__ = Board()
        self.__dados__ = Dice()
        self.__turno__ = self.__jugador1__

    def jugador1(self):
        return self.__jugador1__
    
    def jugador2(self):
        return self.__jugador2__
    
    def tablero(self):
        return self.__tablero__
    
    def dados_tirados(self):
        self.__dados__.tirar()
        return self.__dados__.obtener_movimiento()


    def turno(self):
        return self.__turno__
    
