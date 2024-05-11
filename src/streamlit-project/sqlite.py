import pandas as pd
import streamlit as st

# Carrega os dados do CSV
dados = pd.read_csv("C:/Users/richa/PycharmProjects/streamlit-project/src/datasets/Cidades.csv")

# Exibe um mapa com as cidades
st.map(dados[["latitude", "longitude"]], zoom=5)

# Exibe uma tabela com os dados das cidades
st.dataframe(dados)
