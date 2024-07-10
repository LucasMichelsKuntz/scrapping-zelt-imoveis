class DadosEmissao:    
    """
    Seta os dados base para a consulta, assim deixando o código bem adaptável, caso seja necessário.
    """
    def __init__(self, tipo_contrato="alugar", tipo="apartamento", quartos=1, valor_min=0, valor_max=1800):
        self.tipo_contrato:str = tipo_contrato
        self.tipo:str = tipo
        self.quartos:int = quartos
        self.valor_min:int = valor_min
        self.valor_max:int = valor_max    