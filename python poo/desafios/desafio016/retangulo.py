class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._base = None
        self._altura = None
        self._area = None


        self.base = base
        self.altura = altura


    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("O valor da base deve ser um número!")
        if valor < 0:
            raise ValueError("valor inválido para a base!")
        else:
            self._base = valor


    @property
    def altura(self):
        return self._altura


    @altura.setter
    def altura(self, valor):
        if isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("O valor da altura deve ser um número!")
        if valor < 0:
            raise ValueError("valor inválido para a altura!")
        else:
            self._altura = valor


    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self, area):
        raise PermissionError("Area não pode ser configurada desse jeito!")


    @property
    def medidas(self):
        return f"Base= {self.base}\nAltura= {self.altura} \nArea= {self.area}"

    @medidas.setter
    def medidas(self, valores:tuple):
        if not isinstance(valores, tuple):
            raise TypeError("As medidas devem ser informadas dentro de uma tupla!")
        if len(valores) != 2:
            raise SyntaxError("Informe apenas dois valores numericos!")
        if isinstance(valores[0], float) and not isinstance(valores[0], int):
            self.base = valores[0]
        else:
            raise TypeError("As medidas devem ser informadas!")
        if isinstance(valores[1], float) and not isinstance(valores[1], int):
            self.altura = valores[1]
        else:
            raise TypeError("As medidas devem ser informadas!")

