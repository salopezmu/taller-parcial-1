class ContadorSeguro:
    def __init__(self):
        self._n = 0
    def inc(self):
        self._n += 1
        self.__log()
    @property
    def n(self):
        return self._n
    def __log(self):
        print("tick")

c = ContadorSeguro()
c.inc() # tick
c.inc() # tick
print(c.n) #2