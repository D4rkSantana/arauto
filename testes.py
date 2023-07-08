import pandas as pd

class Teste:
    def tTeste(self, nome:str):
        return nome

    def __init__(self, nome:str):
        self.nome = self.tTeste(nome)
        print(self.nome)

teste = Teste('Ola')