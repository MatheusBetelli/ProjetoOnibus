from abc import abstractclassmethod

class Onibus(abc):
    def __init__(self, codigo, origem, placa, locadoura, assentos):
        self.codigo = codigo
        self.origem = origem
        self.placa = placa
        self.locadoura = locadoura
        self.assentos = assentos