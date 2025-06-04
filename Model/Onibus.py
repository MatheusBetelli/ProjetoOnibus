from Reserva import Reserva

class Onibus:
    def __init__(self, codigo, origem, placa, locadora, assentos):
        self.codigo = codigo
        self.origem = origem
        self.placa = placa
        self.locadora = locadora
        self.assentos = assentos
        self.vendas = []  # vendas associadas

    def numero_vendas(self):
        # Retorna o número de vendas associadas ao ônibus
        return len(self.vendas)

    def verificar_assentos_disponiveis(self):
        # Retorna o número de assentos disponíveis
        return self.assentos - self.numero_vendas()


    def adicionar_venda(self, reserva):
        # Verifica se o assento da reserva já foi ocupado
        if self.numero_vendas() < self.assentos:
            # Verifica se o assento já foi reservado (evitar duplicidade)
            if any(venda.assento == reserva.assento for venda in self.vendas):
                print(f"Assento {reserva.assento} já está ocupado.")
            else:
                self.vendas.append(reserva)
                print(f"Venda adicionada para o assento {reserva.assento}.")
        else:
            print("Não há assentos suficientes no ônibus para essa venda.")



# Teste
onibus = Onibus(codigo=1, origem="São Paulo", placa="ABC1234", locadora="Locadora XYZ", assentos=30)

# Simulando vendas (reservas)
reserva1 = Reserva(codigo=1, data="2025-06-04", preco=100, assento=1, origem="São Paulo", destino="Rio", id_cliente=1)
reserva2 = Reserva(codigo=2, data="2025-06-04", preco=100, assento=2, origem="São Paulo", destino="Rio", id_cliente=2)

onibus.adicionar_venda(reserva1)
onibus.adicionar_venda(reserva2)

# Tentando adicionar uma venda para um assento já ocupado
reserva3 = Reserva(codigo=3, data="2025-06-04", preco=100, assento=1, origem="São Paulo", destino="Rio", id_cliente=3)
onibus.adicionar_venda(reserva3)  # Assento 1 já ocupado

# Verificando o número de vendas e assentos disponíveis
print(f"Vendas realizadas: {onibus.numero_vendas()}")
print(f"Assentos disponíveis: {onibus.verificar_assentos_disponiveis()}")
