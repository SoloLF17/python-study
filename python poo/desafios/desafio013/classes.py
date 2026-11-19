class Termostato:

    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError(f"Temperatura de {valor}{chr(176)}C é invalida")
        if valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = valor

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}{chr(176)}C"