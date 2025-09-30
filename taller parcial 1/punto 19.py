class _Repositorio:
    def __init__(self):
        self._datos = {}
    def guardar(self, k, v):
        self._datos[k] = v
    def _dump(self):
       return dict(self._datos)
class Servicio:
    def __init__(self):
        self.__repo = _Repositorio()
    def guardar(self, clave, valor):
        self.__repo.guardar(clave, valor)

# Expón un método &#39;guardar&#39; que delegue en el repositorio,
# pero NO expongas _dump ni __repo.