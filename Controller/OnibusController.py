from Model.Onibus import Onibus
import sqlite3

def criar_onibus(onibus: Onibus):
    conexao = sqlite3.connect("Rodoviaria.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO onibus (id, origem, placa, nome_locadoura, qtn_assento)
        VALUES (?, ?, ?, ?, ?)""",
        (onibus.codigo, onibus.origem, onibus.placa, onibus.locadora, onibus.assentos)
    )
    conexao.commit()
    conexao.close()

def listar_onibus():
    conexao = sqlite3.connect("Rodoviaria.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM onibus")
    resultado = cursor.fetchall()
    conexao.close()
    return resultado
