
#Importar bibliotecas

import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta

#Criar as funções de carregamento de dados 
     # cotações de algo
@st.cache_data
def carregar_dados (empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    cotacoes_acao = dados_acao.history(period = "1d", start = "2017-01-01", end= "2024-08-31")
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao

#Lista de ações
acoes=["MMM", "HON", "ITW", "EMR", "GE", "BSX", "BAX", "DHR", "CSL", "DRW"]
#carregar dados
dados = carregar_dados(acoes)



# codigo para carregar csv
#@st.cache_data
#def carregar_tickers_acoes():
    #base_tickers = pd.read_csv("IBOV.csv", sep=";")
    #tickers = list(base_tickers["Código"])
    #tickers = [item + "SA" for item in tickers]
    #return tickers

#acoes=carregar_tikers_açoes()
#dados=carregar_dados(acoes)
    

#acoes=["MMM", "HON", "ITW", "EMR", "GE", "BSX", "BAX"]

#dados = carregar_dados(acoes)

#print(dados)

#criar interface streamlit
st.write(""" 
         # Stock Prices over the years
          ### MMM & Competition Close values
         """) # Markdown

# Adicionar imagem e texto adicional na barra lateral
st.sidebar.image("foto_Rui.PNG", caption="Rui Ramos", width=150)  # Substitua "path_to_your_photo.jpg" pelo caminho da sua foto
st.sidebar.write("**Engineer and Data_Scientist**")
st.sidebar.write("Learning is like planting seeds in the mind, and knowledge will always be our most inspiring harvest.")


#Preparar visualizações = filtros
st.sidebar.header("Filters")

#Filtro de acoes

lista_acoes=st.sidebar.multiselect("Select stocks for visualization", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]


#Filtro de datas

data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_data=st.sidebar.slider("Select period", 
                                  min_value=data_inicial , 
                                  max_value=data_final, 
                                  value=(data_inicial, data_final), step=timedelta(days=1))

#Filtra dado pelo intervalo de datas selecionado
dados=dados.loc[intervalo_data[0]:intervalo_data[1]]

# criar o gráfico
st.line_chart(dados)

#Adicionar a legenda abaixo do gráfico
st.write("Filters Applied")
st.write(f"**Selected Stocks:**{', '.join(lista_acoes) if lista_acoes else 'None'}")
st.write(f"**Date Range:** {intervalo_data[0].strftime('%Y-%m-%d')} to {intervalo_data[1].strftime('%Y-%m-%d')}")
texto_performance_ativos = ""

#for ativo in lista_acoes:
    #performance_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1
    #performance_ativo= float(performance_ativo)
    #print(performance_ativo)



st.write(""" 
         ### Rui Ramos 2024
         """) 























