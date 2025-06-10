class Reserva:
    def __init__(self, data, preco, assento, origem, destino, id_cliente, id_venda=None, id=None):
        self.id = id
        self.data = data
        self.preco = preco
        self.assento = assento
        self.origem = origem
        self.destino = destino
        self.id_cliente = id_cliente
        self.id_venda = id_venda