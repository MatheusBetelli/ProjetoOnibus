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
    
    # elif tipo == "Vendas "
                       
        
    else:
        conexao.close()
        return pd.DataFrame()