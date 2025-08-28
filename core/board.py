class Board:
    def __init__(self):
        
        self.__contenedor__ =[
        [],[],[],[],[],[],  [],[],[],[],[],[], [],[],[],[],[],[],  [],[],[],[],[],[]
        ]
        self.__contenedor__[0] = ["Negras"]*2
        self.__contenedor__[11] = ["Negras"]*5
        self.__contenedor__[16] = ["Negras"]*3
        self.__contenedor__[18] = ["Negras"]*5   
       
        self.__contenedor__[5] = ["Blancas"]*5
        self.__contenedor__[7] = ["Blancas"]*3
        self.__contenedor__[12] = ["Blancas"]*5
        self.__contenedor__[23] = ["Blancas"]*2

   