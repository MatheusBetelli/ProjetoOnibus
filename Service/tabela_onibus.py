from database import conectar

conexao = conectar()
cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE onibus (
        id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
        origem TEXT NOT NULL,
        placa TEXT NOT NULL,
        nome_locadoura TEXT NOT NULL,
        qtn_assento INTEGER NOT NULL
        );
"""
)

conexao.commit()
cursor.close()
conexao.close()
print("Tabela Onibus funcionando")