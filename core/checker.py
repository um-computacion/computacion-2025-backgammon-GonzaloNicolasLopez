class Checker:

    def __init__(self, color, posicion=None):
        
        self.color = color
        self.posicion = posicion

    def mover(self, nueva_posicion):
        
        self.posicion = nueva_posicion

    def pieza(self):
        return self.color

    def contenedor(self):
        if self.posicion is not None:
            return self.posicion 

    def __str__(self):
        return f"Ficha {self.color} en posición {self.posicion if self.posicion is not None else 'libre'}"
    
    