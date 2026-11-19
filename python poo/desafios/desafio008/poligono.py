import math
from abc import ABC, abstractmethod

class Poligono(ABC):

    def __init__(self, lados):
        self.lados = lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


class Quadrado(Poligono):
    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2



class Circulo(Poligono):
    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio


    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * self.raio ** 2