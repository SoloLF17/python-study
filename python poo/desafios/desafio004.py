from rich import print
from time import sleep
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Você acabou de abrir o livro [red]{self.titulo}[/] que tem "
              f"[green]{self.total_paginas}[/] paginas no total. Você está agora na pagina [yellow]{self.pagina_atual}[/][blue]")


    def avancar_pagina(self, qtd= 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward:", end='')
                sleep(0.3)
                cont += 1
        print(f"Você avançou {cont} paginas e agora esta na pagina [yellow]{self.pagina_atual}[/][blue]")
        if self.fim_do_livro():
            print(f":closed_book: Você chegou ao final do livro [green]{self.titulo}[/]")
    def fim_do_livro(self) ->bool:
        return True if self.pagina_atual ==  self.total_paginas else False



l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_pagina(10)
