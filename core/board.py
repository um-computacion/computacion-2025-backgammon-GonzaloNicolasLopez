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


    def no_hay_fichas(self, fichas):
        for casilla in self.__contenedor__:
            if casilla is not None and fichas in casilla:
                return False
        return True 
    
    def comer_ficha(self, destino, fichas):
        try:
            if len(self.__contenedor__[destino]) == 1 and self.__contenedor__[destino][0] != fichas:
                rival = self.__contenedor__[destino] [0]
                self.__reserva__[rival] += 1
                self.__contenedor__[destino] = [fichas] 
            if  self.__contenedor__[destino] == None:
                return False 
            if len(self.__contenedor__[destino]) >=2:
                raise ValueError("No se puede mover a esa posición")
                return False
        except (ValueError, AttributeError) as e:
            print(f"Error: {e}")
            return False 
    
    def reserva(self):
        self.__reserva__ ={"Negras":0, "Blancas":0}
        return self.__reserva__ 
    
    def get_contenedor(self):
        return self.__contenedor__


        

         

        
         

   