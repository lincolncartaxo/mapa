import streamlit as st
import pandas as pd
import plotly.express as px

# Exemplo de dados com coordenadas e nomes
df = pd.read_csv("coordenadas.txt", sep=",", encoding="latin1")

# Configurando o modo amplo
#st.set_page_config(layout="wide")

st.title("Mapeamento PNHR")
st.header("Sindicato dos Trabalhadores Rurais de Tavares - Tavares/PB")

# Criar um mapa interativo usando Plotly Express
fig = px.scatter_mapbox(
    df,
    lat='lat',
    lon='lon',
    hover_name='desc',
    zoom=12,
    height=600,
    text='desc'
)

# Configurar o layout para alterar a cor do texto
fig.update_traces(textposition='top right')
fig.update_traces(marker=dict(size=12, color='red'))
fig.update_layout(
    mapbox=dict(
        style="open-street-map"
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    font=dict(color='black')  # cor do texto 
)


# Exibir o mapa no Streamlit
st.plotly_chart(fig)
#st.map(df)
st.dataframe(df)