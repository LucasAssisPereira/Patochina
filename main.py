from crud import Crud
from database import Database
from fabricante import Fabricante
from UF import UF
import os


def main():
    crud = Crud()

    while True:
        option = crud.menu()
        os.system('cls')
        
        match option:
            case 1:
                crud.listar_marcas()
            case 2:
                crud.listar_produto()
            case 3:
                crud.listar_produtos_estados()
            case 4:
                crud.listar_produto_marca()
            case 5:
                crud.apresentar_estado_mais_caro()
            case 6:
                crud.apresentar_fabricante_mais_barato()
            case 7:
                crud.listar_produto_crescente()
            case 8:
                crud.listar_produto_crescente_lucro()
            case 9:
                break
        _ = input('Digite qualquer coisa para sair: ')
        os.system('cls')

if __name__ == '__main__':
    main()