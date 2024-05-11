import numpy as np
import pandas as pd
import streamlit as st
import plotly.figure_factory as ff
import pydeck as pdk

dados_grafico_barras = pd.read_csv(
    'C:/Users/richa/PycharmProjects/streamlit-project/src/datasets/dados_grafico_barras.csv'
)
df_agrupado = dados_grafico_barras.groupby('data').agg(total_transacoes=('total_transacoes', 'sum'),
                                                       categoria_venda_1=('categoria_venda_1', 'sum'),
                                                       categoria_venda_2=('categoria_venda_2', 'sum'))

loc_empresas = pd.read_csv(
    'C:/Users/richa/PycharmProjects/streamlit-project/src/datasets/Cidades.csv'
)
qtd_vendas = pd.read_csv(
    'C:/Users/richa/PycharmProjects/streamlit-project/src/datasets/Vendas.csv'
)
qtd_vendas['data'] = pd.to_datetime(qtd_vendas['data'])
vendas_diarias = qtd_vendas.resample('D', on='data')['quantidade'].mean()

valor_bitcoin = pd.read_csv(
    'https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/3_TwoNumOrdered.csv',
    delimiter=' '
)
valor_bitcoin['date'] = pd.to_datetime(valor_bitcoin['date'])
valor_bitcoin['year'] = valor_bitcoin['date'].dt.year

st.header('Single page application', divider='rainbow')

st.subheader('Mapa simples com latitudes e longitudes')
st.map(loc_empresas[['latitude', 'longitude']], zoom=1)

#st.subheader('Datafrase com os dados utilizados')
#st.dataframe(loc_empresas)

st.subheader('Evolução do valor do bitcoin ao longo do tempo')
#area_chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.area_chart(data=valor_bitcoin, x='date', y='value')
#st.dataframe(valor_bitcoin)

st.subheader('Vendas agrupada por categoria')
bar_chart_data = pd.DataFrame(np.random.randn(25, 3), columns=['carro', 'moto', 'avião'])
st.bar_chart(bar_chart_data)

st.subheader('Evolução das Vendas ao Longo do Tempo')
st.line_chart(data=vendas_diarias, y='quantidade')
#st.dataframe(qtd_vendas)


st.subheader('Scatter chart')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
chart_data['col4'] = np.random.choice(['A', 'B', 'C'], 20)

st.scatter_chart(
    chart_data,
    x='col1',
    y='col2',
    color='col4',
    size='col3',
)

st.subheader('Histograma')
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

st.plotly_chart(fig, use_container_width=True)


st.subheader('3D map')
chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))