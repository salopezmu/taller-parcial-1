class Registro:
    def __init__(self):
        self.__items = []
    def add(self, x):
        self.__items.append(x)
# Crea una propiedad &#39;items&#39; que retorne una tupla inmutable con el contenido
    @property
    def items(self):
        return tuple(self.__items)