#Declaração de class
class Gafanhoto:
    def __init__(self): #Metodo Construtor
    #Atributos de Instancia
     self.nome = ""
     self.idade = 0


    #Metodos de Instancia
    def aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e agora tem {self.idade} anos de idade!"


#Declaraçao de Objetos
g1 = Gafanhoto()
g1.nome = str(input("Nome: "))
g1.idade = int(input("Idade: "))
g1.aniversario()
print(g1.mensagem())
