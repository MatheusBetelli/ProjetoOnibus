from Model.Onibus import Onibus
from Model.Cliente import Cliente
from Model.Reserva import Reserva

class Venda:
    def __init__(self, destino, preco, assento, onibus, cliente, reserva, id=None):
        self.id = id
        self.destino = destino
        self.preco = preco
        self.assento = assento
        self.onibus = onibus
        self.cliente = cliente
        self.reserva = reserva

    def registrar_venda(self):
        return self.onibus.adicionar_venda(self)
