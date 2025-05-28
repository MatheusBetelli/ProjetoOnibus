from abc import abstractclassmethod

class Cliente(ABC):
    def __init__(self, codigo, nome, telefone, nascimento, cpf, cnpg, endereco):
        self.codigo = codigo
        self.nome = nome
        self.telefone = telefone
        self.nascimento = nascimento
        self.cpf = cpf
        self.cnpg = cnpg
        self.endereco = endereco

    def get_codigo(self):
        return self.codigo
    
    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome