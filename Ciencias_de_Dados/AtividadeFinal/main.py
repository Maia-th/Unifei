# Aluno: Thiago Oliveira Maia
# Curso: Ciência e Tecnologia
# Projeto Final: Algoritmo de Aprendizado de Máquina Supervisionado - B3
# Bibliotecas necessárias: pip install yfinance pandas numpy scikit-learn streamlit matplotlib

import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score, confusion_matrix
import streamlit as st
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Dashboard B3 - ML", layout="wide")

plt.rcParams['figure.facecolor'] = '#FFFFFF'
plt.rcParams['axes.facecolor'] = '#FFFFFF'

@st.cache_data
def carregar_e_processar_dados():
    ticker = "ITUB4.SA" 
    df = yf.download(ticker, start="2023-01-01", end="2025-12-31")
    
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel('Ticker')
        
    df.to_csv(f"{ticker}_historico_completo.csv")

    df['Diferenca'] = df['Open'] - df['Close']
    df['Alvo'] = np.where(df['Diferenca'] > 0, 1, 0)
    
    df['Retorno_Diario'] = df['Close'].pct_change()
    df['Media_Movel_5'] = df['Close'].rolling(window=5).mean()
    df['Media_Movel_15'] = df['Close'].rolling(window=15).mean()
    df = df.dropna()
    
    return df

df = carregar_e_processar_dados()

st.title(f"Projeto Final - Aprendizado de Máquina (ITUB4.SA)")

anos_disponiveis = [2023, 2024, 2025]
anos_treino = st.multiselect("Selecione os anos para Treinamento:", anos_disponiveis, default=[2023, 2024])

if anos_treino:
    df_treino = df[df.index.year.isin(anos_treino)].copy()
    df_teste = df[df.index.year == 2025].copy()

    if not df_teste.empty and not df_treino.empty:
        features = ['Open', 'High', 'Low', 'Close', 'Volume', 'Media_Movel_5', 'Media_Movel_15']
        
        scaler = MinMaxScaler()
        X_treino = scaler.fit_transform(df_treino[features])
        y_treino = df_treino['Alvo']
        
        X_teste = scaler.transform(df_teste[features])
        y_teste = df_teste['Alvo']
        
        modelo = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
        modelo.fit(X_treino, y_treino)
        
        previsoes = modelo.predict(X_teste)
        df_teste['Previsao'] = previsoes
        
        acuracia = accuracy_score(y_teste, previsoes)
        precisao = precision_score(y_teste, previsoes, zero_division=0)
        f1 = f1_score(y_teste, previsoes, zero_division=0)
        especificidade = recall_score(y_teste, previsoes, pos_label=0, zero_division=0) 
        
        cm = confusion_matrix(y_teste, previsoes)
        acertos = np.trace(cm)
        erros = np.sum(cm) - acertos
        
        df_teste['Retorno_Estrategia'] = np.where(df_teste['Previsao'] == 1, df_teste['Retorno_Diario'], 0)
        
        retorno_ganhos = df_teste[df_teste['Retorno_Estrategia'] > 0]['Retorno_Estrategia'].sum() * 100
        retorno_perdas = df_teste[df_teste['Retorno_Estrategia'] < 0]['Retorno_Estrategia'].sum() * 100
        retorno_geral = retorno_ganhos + retorno_perdas
        
        st.markdown("### Métricas de Avaliação e Retorno Financeiro")
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col1.metric("Acertos", f"{acertos}")
        col2.metric("Erros", f"{erros}")
        col3.metric("Acurácia", f"{acuracia:.4f}")
        col4.metric("Ganhos", f"{retorno_ganhos:.2f}%")
        col5.metric("Perdas", f"{retorno_perdas:.2f}%")
        col6.metric("Retorno Geral", f"{retorno_geral:.2f}%")
        
        col_g1, col_g2 = st.columns(2)
        
        with col_g1:
            fig1, ax1 = plt.subplots(figsize=(6, 2.5))
            ax1.plot(df.index, df['Close'], color='#00529B', label='Preço de Fechamento')
            ax1.set_title("Evolução do Preço - ITUB4.SA", fontsize=10)
            ax1.set_ylabel("Preço (R$)", fontsize=8)
            ax1.tick_params(axis='both', which='major', labelsize=8)
            ax1.legend(fontsize=8)
            st.pyplot(fig1)
            
        with col_g2:
            contagem_classes = df['Alvo'].value_counts(normalize=True) * 100
            fig2, ax2 = plt.subplots(figsize=(6, 2.5))
            barras = ax2.bar(['Classe 0', 'Classe 1'], contagem_classes.values, color=['#FF0000', '#2ecc71'])
            for i, v in enumerate(contagem_classes.values):
                ax2.text(i, v + 1, f"{v:.2f}%", ha='center', fontsize=8)
            ax2.set_title("Distribuição das Classes", fontsize=10)
            ax2.set_ylabel("Percentual (%)", fontsize=8)
            ax2.tick_params(axis='both', which='major', labelsize=8)
            st.pyplot(fig2)
            
    else:
        st.error("Período selecionado sem dados suficientes para simulação.")