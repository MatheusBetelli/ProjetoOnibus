from database import conectar

conexao = conectar()
cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE venda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        preco REAL NOT NULL,
        assento INTEGER NOT NULL,
        id_onibus INTEGER NOT NULL,
        destino TEXT NOT NULL,
        id_cliente INTEGER NOT NULL,
        id_reserva INTEGER NOT NULL,
        FOREIGN KEY (id_onibus) REFERENCES onibus(id),
        FOREIGN KEY (id_cliente) REFERENCES cliente(id),
        FOREIGN KEY (id_reserva) REFERENCES reserva(id)
        );
"""
)

conexao.commit()
cursor.close()
conexao.close()
print("Tabela Venda funcionando")
