from Model.Reserva import Reserva
import sqlite3
from Service.database import conectar

def criar_reserva(reserva: Reserva):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO reserva (data, id_venda, id_cliente, id_onibus, preco, assento, origem, destino)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (reserva.data, reserva.id_venda, reserva.id_cliente, reserva.id_onibus,
         reserva.preco, reserva.assento, reserva.origem, reserva.destino)
    )
    conexao.commit()
    conexao.close()

def listar_reservas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM reserva")
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

def buscar_reserva(id_reserva):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM reserva WHERE id = ?", (id_reserva,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return Reserva(*resultado)
    else:
        return None