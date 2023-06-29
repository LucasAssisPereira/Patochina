from fabricante import Fabricante
from produto import Produto
from tabulate import tabulate
import sqlite3
import pandas as pd


class Database:
    def connection(self):
        return sqlite3.connect("database.db")

    def db_criar_marca(self, fabricante:Fabricante) -> None:
        query = f"""
        INSERT INTO fabricante(marca, site, telefone, UF)
        VALUES ('{fabricante.marca}', '{fabricante.site}', 
        '{fabricante.telefone}', '{fabricante.uf.sigla}');
        """

        try:
            conn = self.connection()
            cursor = conn.cursor()
            cursor.execute(query)
            print('Novo fabricante adicionado com sucesso.')
        except:
            pass 
        finally:
            conn.close()

    def db_listar_marcas(self) -> None:
        try:
            conn = self.connection()
            df = pd.read_sql_query('SELECT marca, site, telefone, uf FROM fabricante', con=conn)
            print(tabulate(df, headers='keys', tablefmt='psql'))
        except:
            pass 
        finally:
            conn.close()
            
    def db_criar_produto(self) -> None:
        query = f"""
        INSERT INTO produto(nome, valorCompra, valorVenda, valorLucra, percentualLucro, idFabricante) 
        VALUES ('{Produto.nome}','{Produto.valor_compra}','{Produto.valor_venda}','{Produto.get_lucro}', '{Produto.get_percentual_lucro}', '{Produto.idFabricante}' ); """

        try:
            conn = self.connection()
            cursor = conn.cursor(query)
            print('Novo produto adicionado com sucesso')
        except:
            pass 
        finally:
            conn.close()

        
    def db_listar_produtos(self) -> None:
        try:
            conn = self.connection()
            df = pd.read_sql_query('''
            SELECT p.nome, f.marca, p.valorCompra, p.valorVenda, p.valorLucra, p.percentualLucro 
            FROM produto as p 
            inner join fabricante as f 
            on p.idFabricante = f.idFabricante''', con=conn)
            
            print(tabulate(df, headers='keys', tablefmt='psql'))
        except:
            pass 
        finally:
            conn.close()

    def db_listar_produtos_estado(self, sigla:str) -> None:
        try:
            conn = self.connection()
            df = pd.read_sql_query(f"""
            SELECT p.nome, f.marca, p.valorCompra, p.valorVenda, p.valorLucra, p.percentualLucro 
            FROM produto as p 
            inner join fabricante as f 
            on p.idFabricante = f.idFabricante
            WHERE
            f.UF = '{sigla}'""", con=conn)
            
            print(tabulate(df, headers='keys', tablefmt='psql'))
        except:
            pass 
        finally:
            conn.close()

    def db_listar_produtos_marca(self, marca:str) -> None:

        try:
            conn = self.connection()
            df = pd.read_sql_query(f"""
            SELECT p.nome, f.marca, p.valorCompra, p.valorVenda, p.valorLucra, p.percentualLucro 
            FROM produto as p 
            inner join fabricante as f 
            on p.idFabricante = f.idFabricante
            WHERE
            f.marca LIKE '%{marca}%'""", con=conn)
            
            print(tabulate(df, headers='keys', tablefmt='psql'))
        except:
            pass 
        finally:
            conn.close()

    def db_listar_UF_produto_caro(self) -> None:
        try:
            conn = self.connection()
            df = pd.read_sql_query(f"""
            SELECT f.UF 
            FROM 
            fabricante f 
            inner join produto p
            on f.idFabricante = p.idFabricante
            order by p.valorVenda desc
            limit 1""", con=conn)
            
            print(f'UF com produto mais caro: {df["UF"][0]}')
        except:
            pass 
        finally:
            conn.close()

    def db_listar_fabricante_produto_barato(self) -> None:
        try:
            conn = self.connection()
            df = pd.read_sql_query(f"""
            SELECT f.marca
            FROM 
            fabricante f 
            inner join produto p
            on f.idFabricante = p.idFabricante
            order by p.valorVenda asc
            limit 1""", con=conn)
            
            print(f'Marca com produto mais barato: {df["marca"][0]}')
        except:
            pass 
        finally:
            conn.close()

    def db_produto_crescente_valor(self) -> None:
        try:
            conn = self.connection()
            df = pd.read_sql_query('''
            SELECT p.nome, f.marca, p.valorCompra, p.valorVenda, p.valorLucra, p.percentualLucro 
            FROM produto as p 
            inner join fabricante as f 
            on p.idFabricante = f.idFabricante
            order by p.valorVenda asc''', con=conn)
            
            print(tabulate(df, headers='keys', tablefmt='psql'))
        except:
            pass 
        finally:
            conn.close()

    def db_produto_crescente_lucro(self) -> None:
        try:
            conn = self.connection()
            df = pd.read_sql_query('''
            SELECT p.nome, f.marca, p.valorCompra, p.valorVenda, p.valorLucra, p.percentualLucro 
            FROM produto as p 
            inner join fabricante as f 
            on p.idFabricante = f.idFabricante
            order by p.valorLucra asc''', con=conn)
            
            print(tabulate(df, headers='keys', tablefmt='psql'))
        except:
            pass 
        finally:
            conn.close()