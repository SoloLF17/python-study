#Polimorfismo inclusão/override
class Mae:
    def __init__(self, nome:str = "Mamãe"):
        self.nome = nome

    def fazer_pudim(self):
        print(F"{self.nome} faz PUDIM com leite condensado e calda!!")

    def fazer_coxinha(self):
        print(f"{self.nome} frita COXINHA no óleo de soja!!!")



class Filha(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz PUDIM com leite ninho e nutella!!!")



class Filho(Mae):
    def fazer_coxinha(self):
        print(f"{self.nome} faz COXINHA na Air Fryer")