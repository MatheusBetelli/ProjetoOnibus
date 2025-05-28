from abc import abstractclassmethod

class Cliente(ABC):
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = codigo