class UF:
    valid_UFs = {'RO' : 'Rondonia', 
                        'AC' : 'Acre', 
                        'AM' : 'Amazonas', 
                        'RR' : 'Roraima', 
                        'PA' : 'Para', 
                        'AP' : 'Amapa',
                        'TO' : 'Tocantins',
                        'MA' : 'Maranhao',
                        'PI' : 'Piaui',
                        'CE' : 'Ceara', 
                        'RN' : 'Rio Grande do Norte', 
                        'PB' : 'Paraiba',
                        'PE' : 'Pernambuca',
                        'AL' : 'Alagoas',
                        'SE' : 'Sergipe', 
                        'BA' : 'Bahia',
                        'MG' : 'Minas Gerais',
                        'ES' : 'Espirito Santo',
                        'RJ' : 'Rio de Janeiro',
                        'SP' : 'Sao Paulo', 
                        'PR' : 'Parana',
                        'SC' : 'Santa Catarina',
                        'RS' : 'Rio Grande do Sul',
                        'MS' : 'Mato Grosso do Sul',
                        'MT' : 'Mato Grosso', 
                        'GO' : 'Goias',
                        'DF' : 'Distrito Federal'}

    def __init__(self, sigla:str) -> None:
        self.sigla = self._validate_UF(sigla.upper())
        self.nome = self.valid_UFs[self.sigla]

    def _validate_UF(self, sigla) -> str:

        if (sigla not in self.valid_UFs):
            raise ValueError('Sigla de UF invÃ¡lida')
    
        return sigla.upper()