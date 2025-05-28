class Onibus:
    def __init__(self, codigo, origem, placa, locadora, assentos):
        self.codigo = codigo
        self.origem = origem
        self.placa = placa
        self.locadora = locadora
        self.assentos = assentos
        self.vendas = []  # vendas associadas

    def adicionar_venda(self, venda):
        self.vendas.append(venda)
