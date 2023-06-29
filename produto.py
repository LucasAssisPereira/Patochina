from fabricante import Fabricante

class Produto:
    def __init__(self, nome:str, peso:float, valor_compra:float, valor_venda:float, fabricante:Fabricante):
        self.nome = nome
        self.peso = peso
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.fabricante = Fabricante

    def get_lucro(self) -> float:
        return self.valor_venda - self.valor_compra

    def get_percentual_lucro(self) -> float:
        return (self.valor_venda - self.valor_compra) / self.valor_venda * 100
    
    def __repr__(self) -> str:
        return f'Nome: {self.nome} \nPreÃ§o: {self.valor_compra} \nVenda: {self.valor_venda} \nLucro: {self.get_lucro()} \nMargem: {self.get_percentual_lucro()}%'