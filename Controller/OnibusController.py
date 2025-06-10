from Model.Onibus import Onibus
import sqlite3
from Service.database import conectar
from Controller.VendaController import listar_vendas, buscar_assentos_ocupados

def criar_onibus(onibus: Onibus):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO onibus ( origem, placa, nome_locadoura, qtn_assento)
        VALUES (?, ?, ?, ?)""",
        (onibus.origem, onibus.placa, onibus.nome_locadoura, onibus.qtn_assento)
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
        id, origem, placa, nome_locadoura, qtn_assento = resultado
        onibus = Onibus(origem, placa, nome_locadoura, qtn_assento, id=id)
        onibus.vendas = buscar_assentos_ocupados(id)
        return onibus
    else:
        return None