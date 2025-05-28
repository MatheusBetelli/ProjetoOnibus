import sqlite3

conexao = sqlite3.connect("Rodoviaria.db")

cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE cliente (
        id INTEGER PRIMARY KEY NOT NULL,
        cpf TEXT NOT NULL,
        cnpj TEXT NOT NULL,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL,
        nascimento DATE NOT NULL,
        telefone TEXT NOT NULL
        );
"""
)

cursor.close()
print("Tabela Cliente funcionando")