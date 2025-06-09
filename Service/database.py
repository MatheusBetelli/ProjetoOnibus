import os
import sqlite3

server = ''
username = ''
password = ''
database = 'Rodoviaria.db'

CAMINHO_BANCO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', database))

conexao = sqlite3.connect(CAMINHO_BANCO)
print("Banco de dados Empresa Criado com sucesso!")

def conectar():
    return sqlite3.connect(CAMINHO_BANCO)
