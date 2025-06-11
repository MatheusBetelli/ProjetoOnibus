import sys
import os

# Adiciona o diretório raiz do projeto ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from Model.Cliente import Cliente
from Model.Onibus import Onibus
from Model.Reserva import Reserva
from Model.Venda import Venda
from Controller.ClienteController import criar_cliente, listar_clientes, buscar_cliente_por_id
from Controller.OnibusController import criar_onibus, listar_onibus, buscar_onibus_id
from Controller.ReservaController import criar_reserva, listar_reservas, buscar_reserva, buscar_assentos_reservados
from Controller.VendaController import criar_venda, buscar_assentos_ocupados
from Service.tabela_relatorio import gerar_relatorio
from Service.operacoes import mostrar_tabela, atualizar_valor, deletar_por_id, selecionar_id

st.title("Rodoviária - Sistema de Passagens")

menu = st.sidebar.selectbox("Menu", ["Clientes", "Ônibus", "Reservas", "Vendas", "Relatórios", "Tabelas", "Operações CRUD"])

if menu == "Clientes":
    st.header("Cadastro de Cliente")
    nome = st.text_input("Nome")
    telefone = st.text_input("Telefone")
    nascimento = st.date_input("Data de Nascimento")
    cpf = st.text_input("CPF")
    cnpj = st.text_input("CNPJ")
    endereco = st.text_input("Endereço")
    if st.button("Cadastrar Cliente"):
        cliente = Cliente(nome=nome, telefone=telefone, nascimento=str(nascimento), cpf=cpf, cnpj=cnpj, endereco=endereco)
        criar_cliente(cliente)
        st.success("Cliente cadastrado com sucesso!")

    st.subheader("Lista de Clientes")
    for cliente in listar_clientes():
        st.text(cliente)

elif menu == "Ônibus":
    st.header("Cadastro de Ônibus")
    origem = st.text_input("Origem")
    placa = st.text_input("Placa")
    locadora = st.text_input("Locadora")
    assentos = st.number_input("Qtde Assentos", min_value=1, step=1)
    if st.button("Cadastrar Ônibus"):
        onibus = Onibus(origem=origem, placa=placa, nome_locadoura=locadora, qtn_assento=int(assentos))
        criar_onibus(onibus)
        st.success("Ônibus cadastrado com sucesso!")

    st.subheader("Lista de Ônibus")
    for o in listar_onibus():
        st.text(o)

elif menu == "Reservas":
    st.header("Reserva de Passagem")
    data = st.date_input("Data da Viagem")
    preco = st.number_input("Preço")
    assento = st.number_input("Assento", step=1)
    origem = st.text_input("Origem")
    destino = st.text_input("Destino")
    id_onibus = st.number_input("ID do Onibus", step=1)
    id_cliente = st.number_input("ID do Cliente", step=1)

    if st.button("Reservar"):
        cliente = buscar_cliente_por_id(id_cliente)
        onibus = buscar_onibus_id(id_onibus)

        if cliente is None:
            st.error("Cliente não encontrado com esse ID.")
        elif onibus is None:
            st.error("Ônibus não encontrado com esse ID.")
        elif assento not in onibus.verificar_assentos_disponiveis():
            st.error(f"Assento {assento} já está ocupado ou é inválido.")
        else:
            assentos_ocupados = buscar_assentos_ocupados(id_onibus)
            assentos_reservados = buscar_assentos_reservados(id_onibus)
            assentos_indisponiveis = set(assentos_ocupados + assentos_reservados)

            if assento in assentos_indisponiveis:
                st.error(f"Assento {assento} já está ocupado ou reservado.")
            elif assento > onibus.qtn_assento or assento < 1:
                st.error(f"O assento {assento} não existe nesse ônibus.")
            else:
                reserva = Reserva(
                    data=str(data), preco=preco, assento=assento, origem=origem, destino=destino, id_cliente=id_cliente, id_onibus=id_onibus
                )
                criar_reserva(reserva)
                st.success("Reserva realizada com sucesso!")

elif menu == "Vendas":
    st.header("Venda de Passagem")
    preco = st.number_input("Preço da Venda")
    assento = st.number_input("Assento", step=1)
    id_onibus = st.number_input("ID Ônibus", step=1)
    destino = st.text_input("Destino")
    id_cliente = st.number_input("ID Cliente", step=1)
    id_reserva = st.number_input("ID Reserva", step=1)

    if st.button("Registrar Venda"):
        cliente = buscar_cliente_por_id(id_cliente)
        onibus = buscar_onibus_id(id_onibus)
        reserva = buscar_reserva(id_reserva)

        if cliente is None:
            st.error("Cliente não encontrado com esse ID.")
        elif onibus is None:
            st.error("Ônibus não encontrado com esse ID.")
        elif reserva is None:
            st.error("Reserva não encontrada com esse ID.")
        else:
            venda = Venda(preco=preco, assento=assento, onibus=onibus, destino=destino, cliente=cliente, reserva=reserva)
            if venda.registrar_venda():
                criar_venda(venda)
                st.success("Venda registrada com sucesso!")
            else:
                st.error(f"Assento {assento} já está ocupado ou é inválido.")

elif menu == "Relatórios":
    st.header("Relatórios do Sistema de Ônibus")

    opcoes = ["Reservas com Cliente e Ônibus", "Vendas Com Clientes e Reserva", "Cliente que mais comprou"]
    escolha = st.selectbox("Escolha qual Relatório ver ", opcoes)

    if escolha:
        df = gerar_relatorio(escolha)

        if not df.empty:
            st.subheader(f"Relatório: {escolha}")
            st.dataframe(df)
        else:
            st.info("Nenhum dado encontrado para esse relatório.")

elif menu == "Tabelas":
    st.header("Tabelas do Sistema de Ônibus")

    opcoes = ["Cliente", "Onibus", "Reserva", "Venda"]
    escolha = st.selectbox("Escolha qual Tabela ver ", opcoes)

    if escolha:
        df = mostrar_tabela(escolha)

        if not df.empty:
            st.subheader(f"Tabelas: {escolha}")
            st.dataframe(df)
        else:
            st.info("Nenhum dado encontrado para esse relatório.")

elif menu == "Operações CRUD":
    st.header("Visualizar e Alterar Dados")
    
    tabela = st.selectbox("Escolha a Tabela", ["cliente", "Onibus", "reserva", "venda"])

    df = mostrar_tabela(tabela)
    st.dataframe(df)

    st.subheader("Atualizar Registro")
id_alvo = st.number_input("ID do Registro", step=1)
campos = {
    "cliente": ["nome", "telefone", "nascimento", "cpf", "cnpj", "endereco"],
    "onibus": ["origem", "placa", "nome_locadoura", "qtn_assento"],
    "reserva": ["data", "preco", "assento", "origem", "destino", "id_cliente", "id_onibus"],
    "venda": ["preco", "assento", "id_onibus", "destino", "id_cliente", "id_reserva"]
}

# Corrige a chave do selectbox comparando em minúsculas
tabela_lower = tabela.lower()

if tabela_lower in campos:
    campo = st.selectbox("Campo a ser atualizado", campos[tabela_lower], key=f"campo_select_{tabela_lower}")
    novo_valor = st.text_input("Novo valor", key=f"novo_valor_{campo}")

    if st.button("Atualizar", key=f"btn_atualizar_{tabela_lower}_{campo}"):
        if selecionar_id(tabela, id_alvo):
            atualizar_valor(tabela, campo, novo_valor, id_alvo)
            st.success(f"{campo} atualizado com sucesso!")
        else:
            st.error("ID inválido ou não existe")
        
    st.subheader("Deletar Registro")
    id_deletar = st.number_input("ID para deletar", step=1, key="delete_id")
    if st.button("Deletar"):
        if selecionar_id(tabela, id_deletar):
            deletar_por_id(tabela, id_deletar)
            st.success("Registro deletado com sucesso!")

        else:
            st.error("Id inválido ou não existe")