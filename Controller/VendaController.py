from Model.Venda import Venda
import sqlite3
from Service.database import conectar

def criar_venda(venda: Venda):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO venda (id, preco, assento, id_onibus, destino, id_cliente, id_reserva)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (venda.id, venda.preco, venda.assento, venda.onibus.id, venda.destino, venda.cliente.id, venda.reserva.id)
    )
    conexao.commit()
    conexao.close()

def listar_vendas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM venda")
    resultado = cursor.fetchall()
    conexao.close()
    return resultado