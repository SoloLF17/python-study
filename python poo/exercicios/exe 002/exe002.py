#Declaração de class
class Gafanhoto:
    def __init__(self,name = "", age = 0): #Metodo Construtor
    #Atributos de Instancia
     self.name = name
     self.age = age


    #Metodos de Instancia
    def aniversario(self):
        self.age += 1


    def __str__(self):
        return f"{self.name} é Gafanhoto(a) e agora tem {self.age} anos de idade!"
#Declaraçao de Objeto
g1 = Gafanhoto("MARIA", 20)

print(g1)
