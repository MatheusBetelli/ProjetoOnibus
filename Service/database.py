# Service/database.py
import os
import sqlite3

# Configurações simuladas (não são usadas no SQLite, mas mantidas se futuramente usar outro SGBD)
server = ''
username = ''
password = ''
database = 'Rodoviaria.db'

# Caminho absoluto correto para o banco na raiz do projeto
CAMINHO_BANCO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', database))

# Cria a conexão com o banco
conexao = sqlite3.connect(CAMINHO_BANCO)
print("Banco de dados Empresa Criado com sucesso!")

# Função para usar em outros arquivos:
def conectar():
    return sqlite3.connect(CAMINHO_BANCO)
