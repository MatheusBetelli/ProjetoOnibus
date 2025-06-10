from database import conectar

conexao = conectar()
cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE reserva (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE NOT NULL,
        id_venda INTEGER NOT NULL,
        id_cliente INTEGER NOT NULL,
        id_onibus INTEGER NOT NULL,
        preco REAL NOT NULL,
        assento INTEGER NOT NULL,
        origem TEXT NOT NULL,
        destino TEXT NOT NULL,
        FOREIGN KEY (id_venda) REFERENCES venda(id),
        FOREIGN KEY (id_cliente) REFERENCES cliente(id),
        FOREIGN KEY (id_onibus) REFERENCES onibus(id)
        );
"""
)

conexao.commit()
cursor.close()
conexao.close()
print("Tabela Reserva funcionando")