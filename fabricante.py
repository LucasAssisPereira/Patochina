from UF import UF

class Fabricante:
    def __init__(self, marca:str, site:str, telefone:str, UF:UF) -> None:
        self.marca = marca 
        self.site = site 
        self.telefone = telefone
        self.UF = UF 