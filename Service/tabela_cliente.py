from database import conectar

conexao = conectar()
cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf TEXT NOT NULL,
        cnpj TEXT NOT NULL,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL,
        nascimento DATE NOT NULL,
        telefone TEXT NOT NULL
        );
"""
)

conexao.commit()
cursor.close()
conexao.close()
print("Tabela Cliente funcionando")