class Reserva:
    def __init__(self, codigo, data, preco, assento, origem, destino, id_cliente, id_venda=None):
        self.codigo = codigo
        self.data = data
        self.preco = preco
        self.assento = assento
        self.origem = origem
        self.destino = destino
        self.id_cliente = id_cliente
        self.id_venda = id_venda
