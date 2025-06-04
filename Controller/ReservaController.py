from Model.Reserva import Reserva
import sqlite3

def criar_reserva(reserva: Reserva):
    conexao = sqlite3.connect("Rodoviaria.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO reserva (id, data, id_venda, id_cliente, preco, assento, origem, destino)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (reserva.codigo, reserva.data, reserva.id_venda, reserva.id_cliente,
         reserva.preco, reserva.assento, reserva.origem, reserva.destino)
    )
    conexao.commit()
    conexao.close()

def listar_reservas():
    conexao = sqlite3.connect("Rodoviaria.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM reserva")
    resultado = cursor.fetchall()
    conexao.close()
    return resultado
