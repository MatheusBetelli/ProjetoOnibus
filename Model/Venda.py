class Venda:
    def __init__(self, codigo, destino, preco, assento, onibus):
        self.codigo = codigo
        self.destino = destino
        self.preco = preco
        self.assento = assento
        self.onibus = onibus
        onibus.adicionar_venda(self)
