class Venda:
    def __init__(self, id, data, preco, assento, destino, id_cliente, id_reserva=None, id_onibus=None):
        self.id = id
        self.data = data
        self.preco = preco
        self.assento = assento
        self.destino = destino
        self.id_cliente = id_cliente
        self.id_reserva = id_reserva
        self.id_onibus = id_onibus
