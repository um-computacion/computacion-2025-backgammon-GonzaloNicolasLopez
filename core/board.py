class Board:
    def __init__(self):

        self.__reserva__ ={"Negras":0, "Blancas":0}
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
        elif color == "Blancas" and destino <= origen :
            return False
        elif color == "Negras" and destino >= origen :
            return False
        elif not self.__contenedor__[origen] :
            return False 
        elif  self.__contenedor__[origen][0] != color:
            return False
        else:
            if self.__contenedor__[destino] == []:
               self.__contenedor__[destino] = [color]
            elif self.__contenedor__[destino][0] == color:    
                self.__contenedor__[destino].append(color)
            self.__contenedor__[origen].pop()


    def no_hay_fichas(self, fichas):
        for casilla in self.__contenedor__:
            if casilla is not None and fichas in casilla:
                return False
        return True 
    
    def comer_ficha(self, destino, fichas):
        if len(self.__contenedor__[destino]) == 1 and self.__contenedor__[destino][0] != fichas:
            rival = self.__contenedor__[destino] [0]
            self.__reserva__[rival] += 1
            self.__contenedor__[destino] = [fichas] 
        elif  self.__contenedor__[destino] == []:
            return False 
        elif len(self.__contenedor__[destino]) >=2:
            return False
        
    
    def reserva(self):
        self.__reserva__ ={"Negras":0, "Blancas":0}
        return self.__reserva__ 
    
    def get_contenedor(self):
        return self.__contenedor__

    def movimiento_correcto(self, origen, destino, color):
        if self.__reserva__[color] > 0:
            return False
        elif not (0 <= origen < len(self.__contenedor__)):
            return False
        elif not (0 <= destino < len(self.__contenedor__)):
            return False
        inicio = self.__contenedor__[origen]
        fin = self.__contenedor__[destino]
        if not inicio:
            return False
        elif not fin:
            return True
        elif fin[0] == color:
            return True
        elif len(fin) == 1 and fin[0] != color:
            return True
        return False
        

         

        
         

   