IA utilizada
CHAT GPT -4.1

class checker

class Checker:
    def __init__(self, color):
        """
        Inicializa una ficha de backgammon.

        Args:
            color (str): Color de la ficha ('blanco' o 'negro').
        """
        self.color = color

    def __str__(self):
        return f"Ficha {self.color}"