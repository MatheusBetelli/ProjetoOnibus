import sqlite3

conexao = sqlite3.connect("Rodoviaria.db")

cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE venda (
        id INTEGER PRIMARY KEY NOT NULL,
        preco REAL NOT NULL,
        assento INTEGER NOT NULL,
        id_onibus INTEGER NOT NULL,
        destino TEXT NOT NULL,
        id_cliente INTEGER NOT NULL,
        id_reserva INTEGER NOT NULL,
        FOREIGN KEY (id_onibus) REFERENCES onibus(id),
        FOREIGN KEY (id_cliente) REFERENCES cliente(id)
        FOREIGN KEY (id_reserva) REFERENCES reserva(id)
        );
"""
)

conexao.commit()
cursor.close()
conexao.close()
print("Tabela Venda funcionando")