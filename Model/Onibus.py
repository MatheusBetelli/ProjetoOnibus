from Model.Reserva import Reserva

class Onibus:
    def _init_(self, id, origem, placa, nome_locadoura, qtn_assento):
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



# # Teste
# onibus = Onibus(id=1, origem="São Paulo", placa="ABC1234", nome_locadora="Locadora XYZ", assentos=30)

# # Simulando vendas (reservas)
# reserva1 = Reserva(id=1, data="2025-06-04", preco=100, assentos=1, origem="São Paulo", destino="Rio", id_cliente=1)
# reserva2 = Reserva(id=2, data="2025-06-04", preco=100, assentos=2, origem="São Paulo", destino="Rio", id_cliente=2)

# onibus.adicionar_venda(reserva1)
# onibus.adicionar_venda(reserva2)

# # Tentando adicionar uma venda para um assento já ocupado
# reserva3 = Reserva(id=3, data="2025-06-04", preco=100, assentos=1, origem="São Paulo", destino="Rio", id_cliente=3)
# onibus.adicionar_venda(reserva3)  # Assento 1 já ocupado

# # Verificando o número de vendas e assentos disponíveis
# print(f"Vendas realizadas: {onibus.numero_vendas()}")
# print(f"Assentos disponíveis: {onibus.verificar_assentos_disponiveis()}")