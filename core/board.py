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

    def mover_ficha(self, origen, destino, color):
        destino = int(destino)
        origen = int(origen)
        if origen < 0 or origen > 23 or destino < 0 or destino > 23:
            return False
        if color == "Blancas" and destino <= origen :
            return False
        if color == "negras" and destino >= origen :
            return False
        if not self.__contenedor__[origen] :
            return False 
        if  self.__contenedor__[origen][0] != color:
            return False
        else:
            if self.__contenedor__[destino] == []:
               self.__contenedor__[destino] = [color]
               self.__contenedor__[origen].pop()
            if self.__contenedor__[destino][0] == color:    
                 self.__contenedor__[destino].append(color)
                 self.__contenedor__[origen].pop()

    

        

         

        
         

   