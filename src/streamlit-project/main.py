import pandas as pd
import streamlit as st

# Define a latitude e longitude do ponto fixo
latitude = -30.0311  # Latitude de Porto Alegre
longitude = -51.1862  # Longitude de Porto Alegre

# Carrega os dados do CSV
dados = pd.read_csv("C:/Users/richa/PycharmProjects/streamlit-project/src/datasets/Cidades.csv")

# Exibe um mapa com as cidades
st.map(data=dados[["latitude", "longitude"]], zoom=1)

# Exibe uma tabela com os dados das cidades
#st.dataframe(dados)
