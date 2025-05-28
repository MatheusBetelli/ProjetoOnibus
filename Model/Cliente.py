from abc import abstractclassmethod

class Cliente(ABC):
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = codigo

    def get_codigo(self):
        return self.codigo
    
    def set_codigo(self, codigo):
        self.codigo = codigo