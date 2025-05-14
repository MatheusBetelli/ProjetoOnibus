# Services/database.py
import sqlite3

server = ''
username = ''
password = ''
database = 'Rodoviaria.db'
conexao = sqlite3.connect(database)
print("Banco de dados Empresa Criado com sucesso! ")