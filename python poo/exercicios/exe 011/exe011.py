from abc import ABC, abstractmethod

# se não tiver metodo propio ele herda
# Polimorfismo; Inclusão: quando um metodo sobrescreve o
# override/subtyping um metodo da mãe, exigi herança
# Sobrecarga; Overloading Ad-Hoc, serve para isso ou para essa finalidade


#polimorfismo de inclusão
class Animal(ABC):
    def __init__(self, nome:str = ''):
        self.nome = nome

    @abstractmethod
    def emitir_soma(self):
        print(f"{self.nome} é {self.__class__.__name__} e está emitindo um som!")



class Pato(Animal):
    def emitir_soma(self):
        print(f"{self.nome} acabou de dizer 'QUACK! QUACK! QUACK!'")


class Cachorro(Animal):
    def emitir_soma(self):
        print(f"{self.nome} acabou de dizer 'AU! AU! AU!'")

class Spitze(Cachorro):
    def emitir_soma(self):
        print(f"{self.nome} acabou de dizer 'au! au! au! au! au! au! au! au! au! au!' ")


class Pitbull(Cachorro):
    def emitir_soma(self):
        print(f"{self.nome} acabou de dizer 'RUF! RUF! RUF!'")



class Gato(Animal):
    def emitir_soma(self):
        print(f"{self.nome} acabou de dizer 'MIAU! MIAU! MIAU!'")



class Galinha(Animal):
    def emitir_soma(self):
        print(f"{self.nome} acabou de dizer 'PÓ! PÓ! PÓ!'")