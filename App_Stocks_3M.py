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
    cotacoes_acao = dados_acao.history(period = "1d", start = "2020-01-01", end= "2024-08-31")
    
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao

acoes=["MMM", "HON", "ITW", "EMR", "GE", "BSX", "BAX"]

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

dados=dados.loc[intervalo_data[0]:intervalo_data[1]]

# criar o gráfico

st.line_chart(dados)

texto_performance_ativos = ""

#for ativo in lista_acoes:
    #performance_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1
    #performance_ativo= float(performance_ativo)
    #print(performance_ativo)



st.write(""" 
         ### Actives performance
         This was the performance of each active in the selected period:

         {under construction}
         """) 























