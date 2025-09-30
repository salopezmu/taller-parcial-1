class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
# Implementa property para nombre

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise TypeError("El nombre debe ser una cadena (str)")
        self._nombre = value