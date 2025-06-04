from Model.Cliente import Cliente
import sqlite3

def criar_cliente(cliente: Cliente):
    conexao = sqlite3.connect("Rodoviaria.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO cliente (id, cpf, cnpj, nome, endereco, nascimento, telefone)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (cliente.codigo, cliente.cpf, cliente.cnpg, cliente.nome, cliente.endereco, cliente.nascimento, cliente.telefone)
    )
    conexao.commit()
    conexao.close()

def listar_clientes():
    conexao = sqlite3.connect("Rodoviaria.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM cliente")
    clientes = cursor.fetchall()
    conexao.close()
    return clientes
