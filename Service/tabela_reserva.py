import sqlite3

conexao = sqlite3.connect("Rodoviaria.db")

cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE reserva (
        id INTEGER PRIMARY KEY NOT NULL,
        data DATE NOT NULL,
        id_venda INTEGER NOT NULL,
        id_cliente INTEGER NOT NULL,
        preco REAL NOT NULL,
        assento INTEGER NOT NULL,
        origem TEXT NOT NULL,
        destino TEXT NOT NULL,
        FOREIGN KEY (id_venda) REFERENCES venda(id),
        FOREIGN KEY (id_cliente) REFERENCES cliente(id)
        );
"""
)


cursor.close()
print("Tabela Reserva funcionando")