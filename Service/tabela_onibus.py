import sqlite3

conexao = sqlite3.connect("Rodoviaria.db")

cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE onibus (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        origem TEXT NOT NULL,
        placa TEXT NOT NULL,
        nome_locadoura TEXT NOT NULL,
        qtn_assento INTEGER NOT NULL
        );
"""
)

cursor.close()
print("Tabela Onibus funcionando")