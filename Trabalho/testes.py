import datetime


class Planta:
    def __init__(self):
        self.valor = 3
        self.total = 0

    def somar(self):
        self.total = self.valor + 3

    def somarValor(self, outroValor: int):
        self.total = self.valor + outroValor

    def getSoma(self):
        return self.total


novaPlanta = Planta()
novaPlanta.somarValor(6)
print(novaPlanta.getSoma())
