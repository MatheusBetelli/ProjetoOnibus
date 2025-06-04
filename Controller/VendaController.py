from Model.Venda import Venda
import sqlite3

def criar_venda(venda: Venda):
    conexao = sqlite3.connect("Rodoviaria.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO venda (id, preco, assento, id_onibus, destino, id_cliente, id_reserva)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (venda.codigo, venda.preco, venda.assento, venda.onibus.codigo, venda.destino, venda.onibus.vendas[-1].id_cliente, venda.onibus.vendas[-1].codigo)
    )
    conexao.commit()
    conexao.close()

def listar_vendas():
    conexao = sqlite3.connect("Rodoviaria.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM venda")
    resultado = cursor.fetchall()
    conexao.close()
    return resultado
