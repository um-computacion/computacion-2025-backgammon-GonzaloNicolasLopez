class Player:
     def __init__(self, nombre, color):
        
        self.__nombre__ = nombre
        self.__color__ = color


     def __str__(self):
        return f"{self.__nombre__} {self.__color__}"

