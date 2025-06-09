from Model.Onibus import Onibus
import sqlite3
from Service.database import conectar

def criar_onibus(onibus: Onibus):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO onibus (id, origem, placa, nome_locadoura, qtn_assento)
        VALUES (?, ?, ?, ?, ?)""",
        (onibus.id, onibus.origem, onibus.placa, onibus.nome_locadoura, onibus.qtn_assento)
    )
    conexao.commit()
    conexao.close()

def listar_onibus():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM onibus")
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

def buscar_onibus_id(id_onibus):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM onibus WHERE ID = ?", (id_onibus,))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return Onibus(*resultado)
    else:
        return None