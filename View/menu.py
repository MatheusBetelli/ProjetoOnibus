import streamlit as st
from Model.Onibus import Onibus
from Model.Cliente import Cliente
from Model.Reserva import Reserva
from Model.Venda import Venda
from Controller.ClienteController import criar_cliente, listar_clientes
from Controller.OnibusController import criar_onibus, listar_onibus
from Controller.ReservaController import criar_reserva, listar_reservas
from Controller.VendaController import criar_venda, listar_vendas

st.title("Rodoviária - Sistema de Passagens")

menu = st.sidebar.selectbox("Menu", ["Clientes", "Ônibus", "Reservas", "Vendas"])

if menu == "Clientes":
    st.header("Cadastro de Cliente")
    codigo = st.number_input("Código", step=1)
    nome = st.text_input("Nome")
    telefone = st.text_input("Telefone")
    nascimento = st.date_input("Data de Nascimento")
    cpf = st.text_input("CPF")
    cnpj = st.text_input("CNPJ")
    endereco = st.text_input("Endereço")
    if st.button("Cadastrar Cliente"):
        cliente = Cliente(codigo, nome, telefone, str(nascimento), cpf, cnpj, endereco)
        criar_cliente(cliente)
        st.success("Cliente cadastrado com sucesso!")

    st.subheader("Lista de Clientes")
    for cliente in listar_clientes():
        st.text(cliente)

elif menu == "Ônibus":
    st.header("Cadastro de Ônibus")
    codigo = st.number_input("Código", step=1)
    origem = st.text_input("Origem")
    placa = st.text_input("Placa")
    locadora = st.text_input("Locadora")
    assentos = st.number_input("Qtde Assentos", min_value=1, step=1)
    if st.button("Cadastrar Ônibus"):
        onibus = Onibus(codigo, origem, placa, locadora, assentos)
        criar_onibus(onibus)
        st.success("Ônibus cadastrado com sucesso!")

    st.subheader("Lista de Ônibus")
    for o in listar_onibus():
        st.text(o)

elif menu == "Reservas":
    st.header("Reserva de Passagem")
    codigo = st.number_input("Código da Reserva", step=1)
    data = st.date_input("Data da Viagem")
    preco = st.number_input("Preço")
    assento = st.number_input("Assento", step=1)
    origem = st.text_input("Origem")
    destino = st.text_input("Destino")
    id_cliente = st.number_input("ID do Cliente", step=1)
    id_venda = st.number_input("ID da Venda", step=1)
    if st.button("Reservar"):
        reserva = Reserva(codigo, str(data), preco, assento, origem, destino, id_cliente, id_venda)
        criar_reserva(reserva)
        st.success("Reserva realizada com sucesso!")

    st.subheader("Lista de Reservas")
    for r in listar_reservas():
        st.text(r)

elif menu == "Vendas":
    st.header("Venda de Passagem")
    codigo = st.number_input("Código da Venda", step=1)
    preco = st.number_input("Preço da Venda")
    assento = st.number_input("Assento", step=1)
    id_onibus = st.number_input("ID Ônibus", step=1)
    destino = st.text_input("Destino")
    id_cliente = st.number_input("ID Cliente", step=1)
    id_reserva = st.number_input("ID Reserva", step=1)
    if st.button("Registrar Venda"):
        # Aqui criamos um objeto de venda simulando um ônibus com os dados mínimos
        onibus_fake = Onibus(id_onibus, "", "", "", 50)
        reserva_fake = Reserva(id_reserva, "", preco, assento, "", destino, id_cliente)
        onibus_fake.adicionar_venda(reserva_fake)
        venda = Venda(codigo, destino, preco, assento, onibus_fake)
        criar_venda(venda)
        st.success("Venda registrada com sucesso!")

    st.subheader("Lista de Vendas")
    for v in listar_vendas():
        st.text(v)
