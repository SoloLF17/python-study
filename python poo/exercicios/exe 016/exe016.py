#polimorfismo Duck typing, não importo o tipo do objeto importa se ele sabe fazer alguma coisa

class Porta:
    def abrir(self):
        print("Girar a maçaneta e empurrar/puxar a porta!")

class Empresa:
    def abrir(self):
        print("Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ!")

class Ovo:
    def abrir(self):
        print("Quebre a casca com um garfo e separe as partes sobre uma frigideira!")

class Pedra:
    pass


#Metodo pythonico polimorfico duck typing

def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei problemas ao tentar abrir um objeto tipo {objeto.__class__.__name__}!")
