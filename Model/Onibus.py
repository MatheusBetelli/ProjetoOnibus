from Model.Reserva import Reserva

class Onibus:
    def __init__(self, origem, placa, nome_locadoura, qtn_assento, id=None):
        self.id = id
        self.origem = origem
        self.placa = placa
        self.nome_locadoura = nome_locadoura
        self.qtn_assento = int(qtn_assento)
        self.vendas = []  # vendas associadas

    def numero_vendas(self):
        # Retorna o número de vendas associadas ao ônibus
        return len(self.vendas)

    def verificar_assentos_disponiveis(self):
        # Retorna a lista de assentos disponíveis
        assentos_ocupados = set(self.vendas)
        return [i for i in range(1, self.qtn_assento + 1) if i not in assentos_ocupados]

    def adicionar_venda(self, venda):
        assentos_disponiveis = self.verificar_assentos_disponiveis()

        if venda.assento not in assentos_disponiveis:
            # print(f"Assento {venda.assento} já está ocupado ou é inválido.")
            return False

        self.vendas.append(venda)
        # print(f"Venda adicionada com sucesso para o assento {venda.assento}.")
        return True
