import sqlite3
from database import conectar

conexao = conectar()

cursor = conexao.cursor()

cursor.execute("CREATE INDEX IF NOT EXISTS index_cliente ON venda(id_onibus);")
cursor.execute("CREATE INDEX IF NOT EXISTS index_cliente ON venda(id_cliente);")
cursor.execute("CREATE INDEX IF NOT EXISTS index_cliente ON venda(id_reserva);")
cursor.execute("CREATE INDEX IF NOT EXISTS index_cliente ON reserva(id_cliente);")
cursor.execute("CREATE INDEX IF NOT EXISTS index_cliente ON reserva(id_onibus);")

conexao.commit()

cursor.close()

print("INDEX CRIADO COM SUCESSO")