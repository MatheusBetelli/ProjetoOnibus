from Model.Cliente import Cliente
import sqlite3
from Service.database import conectar

clientes = [] 


def criar_cliente(cliente: Cliente):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO cliente (cpf, cnpj, nome, endereco, nascimento, telefone)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (cliente.cpf, cliente.cnpj, cliente.nome, cliente.endereco, cliente.nascimento, cliente.telefone)
    )
    conexao.commit()
    conexao.close()

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM cliente")
    clientes = cursor.fetchall()
    conexao.close()
    return clientes

def buscar_cliente_por_id(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM cliente WHERE id = ?", (id_cliente,))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return Cliente(*resultado)
    else:
        return None