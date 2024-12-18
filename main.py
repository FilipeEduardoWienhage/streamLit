import streamlit as st
import pandas as pd
import yfinance as yf



def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes_acao = dados_acao.history(period='1d', start='2010-01-01', end='2024-12-18')
    cotacoes_acao = cotacoes_acao[['Close']]
    return cotacoes_acao


dados = carregar_dados("ITUB4.SA")
print(dados)


st.write("""
# App preço da ação ITUB4
O gráfico abaixo representa a evolução do preço da ação ITUB4 ao longo dos anos
""") # markdown

st.line_chart(dados)