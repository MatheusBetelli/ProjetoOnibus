from Service.database import conectar
import pandas as pd

def mostrar_tabela(nome_tabela):
    conexao = conectar()
    try:
        df = pd.read_sql_query(f"SELECT * FROM {nome_tabela}", conexao)
        return df
    except Exception as e:
        print(f"Erro ao mostrar tabela {nome_tabela}: {e}")
        return pd.DataFrame()
    finally:
        conexao.close()

def deletar_por_id(nome_tabela, id_valor):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(f"DELETE FROM {nome_tabela} WHERE id = ?", (id_valor,))
    conexao.commit()
    conexao.close()

def atualizar_valor(nome_tabela, campo, novo_valor, id_valor):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(f"UPDATE {nome_tabela} SET {campo} = ? WHERE id = ?", (novo_valor, id_valor))
    conexao.commit()
    conexao.close()

def selecionar_id(nome_tabela, id_tabela):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(f"SELECT 1 FROM {nome_tabela} WHERE id = ?", (id_tabela,))
    existe = cursor.fetchone() is not None
    conexao.close()

    return existe