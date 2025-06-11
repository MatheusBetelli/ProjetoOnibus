import pandas as pd
from Service.database import conectar


def gerar_relatorio(tipo):
    conexao = conectar()

    if tipo == "Reservas com Cliente e Ônibus":
        query = """
            SELECT r.id, r.assento, c.nome AS cliente_nome, o.placa AS onibus_placa
                       FROM reserva r
                       LEFT JOIN cliente c ON r.id_cliente = c.id
                       LEFT JOIN onibus o ON r.id_onibus = o.id
    """
        df = pd.read_sql(query,conexao)
        conexao.close()
        return df
    
    elif tipo == "Vendas Com Clientes e Reserva":
        query = """
            SELECT v.id, v.preco, v.assento, v.id_onibus, c.nome AS cliente_nome,  o.placa AS onibus_placa
                FROM venda v
                JOIN cliente c ON v.id_cliente = c.id
                JOIN onibus o ON v.id_onibus = o.id
        """
        df = pd.read_sql_query(query, conexao)
        conexao.close()
        return df

    elif tipo == "Cliente que mais comprou":
        query = """
        SELECT c.id AS cliente_id, c.nome AS nome_cliente,
        COALESCE(v.total_venda, 0) + COALESCE(r.total_reserva, 0) AS Preco_investido
        FROM cliente c
        LEFT JOIN (
            SELECT id_cliente, SUM(preco) AS total_venda
            FROM venda
            GROUP BY id_cliente
        ) v ON v.id_cliente = c.id
        LEFT JOIN (
            SELECT id_cliente, SUM(preco) AS total_reserva
            FROM reserva
            GROUP BY id_cliente
        ) r ON r.id_cliente = c.id
        ORDER BY Preco_investido DESC;

"""    
        df = pd.read_sql_query(query, conexao)
        conexao.close()
        return df
    


    else:
        conexao.close()
        return pd.DataFrame()