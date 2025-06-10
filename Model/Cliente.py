class Cliente:
    def __init__(self, id, nome, telefone, nascimento, cpf, cnpj, endereco):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.nascimento = nascimento
        self.cpf = cpf
        self.cnpj = cnpj
        self.cnpj = cnpj
        self.endereco = endereco

    def get_codigo(self):
        return self.codigo
    
    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome