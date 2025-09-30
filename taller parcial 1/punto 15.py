class Motor:
    def __init__(self, velocidad):
        self.velocidad = velocidad # refactor aquí
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, value):
        if 0 <= value <= 200:
            self._velocidad = value