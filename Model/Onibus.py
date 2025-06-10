# from Model.Reserva import Reserva

class Onibus:
    def __init__(self, id, origem, placa, nome_locadoura, qtn_assento):
        self.id = id
        self.origem = origem
        self.placa = placa
        self.nome_locadoura = nome_locadoura
        self.qtn_assento = qtn_assento
        self.vendas = []  # vendas associadas

    def numero_vendas(self):
        # Retorna o número de vendas associadas ao ônibus
        return len(self.vendas)

    def verificar_assentos_disponiveis(self):
        # Retorna o número de assentos disponíveis
        return self.qtn_assento - self.numero_vendas()


    def adicionar_venda(self, venda):
        # Verifica se o assento da reserva já foi ocupado
        if self.numero_vendas() < self.qtn_assento:
            # Verifica se o assento já foi reservado (evitar duplicidade)
            if any(venda.assento == venda.assento for venda in self.vendas):
                print(f"Assento {venda.assento} já está ocupado.")
            else:
                self.vendas.append(venda)
                print(f"Venda adicionada para o assento {venda.assento}.")
        else:
            print("Não há assentos suficientes no ônibus para essa venda.")
