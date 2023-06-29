from UF import UF
from database import Database
from time import sleep
import os


class Crud:
    def __init__(self):
        self.sql = Database()

    def menu(self):
        options = [x for x in range(1, 10)]
        op = 0
        
        while (op not in options):
            print(f'{"=-" * 20} MENU PATOCHINA {"=-" * 20}')
            print('1 - Listar todas as marcas;')
            print('2 - Listar todos os produtos;')
            print('3 - Listar produtos por estado;')
            print('4 - Listar produtos por marca;')
            print('5 - Estado com produto mais caro;')
            print('6 - Fabricante mais barato;')
            print('7 - Produtos em ordem crescente por valor;')
            print('8 - Produtos em ordem crescente por valor de lucro;')
            print('9 - Sair;')
            print(f'{"=-" * 20} MENU PATOCHINA {"=-" * 20}')
            op = int(input('Digite sua opção: '))

            if (op not in options):
                print('Opção inválida')
                sleep(2)
                os.system('cls')

        return op 
        
    def listar_marcas(self):
        self.sql.db_listar_marcas()

    def listar_produto(self):
        self.sql.db_listar_produtos()

    def listar_produtos_estados(self):
        while True:
            try:
                sigla = str(input('UF: '))
                uf = UF(sigla)
                self.sql.db_listar_produtos_estado(sigla=uf.sigla)
                break
            except ValueError:
                continue

    def listar_produto_marca(self):
        marca = str(input("Marca: "))
        self.sql.db_listar_produtos_marca(marca)

    def apresentar_estado_mais_caro(self):
        self.sql.db_listar_UF_produto_caro()

    def apresentar_fabricante_mais_barato(self):
        self.sql.db_listar_fabricante_produto_barato()

    def listar_produto_crescente(self):
        self.sql.db_produto_crescente_valor()
    
    def listar_produto_crescente_lucro(self):
        self.sql.db_produto_crescente_lucro()