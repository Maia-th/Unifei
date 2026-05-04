import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Messi Goals", layout="wide")

st.markdown("""
    <style>
        .block-container { padding-top: 1rem; padding-bottom: 0rem; }
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("⚽ Dashboard: Gols de Lionel Messi (2004-2026)")

@st.cache_data
def load_data():
    df = pd.read_csv("messi_all_goals.csv")
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    return df

df = load_data()

col_top1, col_top2 = st.columns([1, 3])

with col_top1:
    st.subheader("Filtro de Período")
    anos = sorted(df['year'].dropna().unique().tolist())
    anos.insert(0, "Toda a Carreira")
    ano_selecionado = st.selectbox("Selecione o Ano:", anos)

if ano_selecionado == "Toda a Carreira":
    df_filtrado = df
else:
    df_filtrado = df[df['year'] == ano_selecionado]

with col_top2:
    # Mostrando a tabela com altura reduzida para não gerar rolagem na página
    st.dataframe(df_filtrado[['date', 'club', 'opponent', 'goal_minute', 'goal_type', 'competition']], height=150, use_container_width=True)

st.markdown("---")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Gráfico 1: Linha (Evolução de gols ao longo dos meses/anos)
with col1:
    gols_tempo = df_filtrado.groupby(df_filtrado['date'].dt.to_period("M")).size().reset_index(name='Gols')
    gols_tempo['date'] = gols_tempo['date'].dt.to_timestamp()
    fig_linha = px.line(gols_tempo, x='date', y='Gols', title='📈 Evolução de Gols no Tempo', height=280)
    fig_linha.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_linha, use_container_width=True)

# Gráfico 2: Barra (Gols por tipo/parte do corpo)
with col2:
    gols_tipo = df_filtrado['goal_type'].value_counts().reset_index()
    gols_tipo.columns = ['Tipo de Gol', 'Quantidade']
    fig_barra = px.bar(gols_tipo, x='Tipo de Gol', y='Quantidade', title='📊 Gols por Tipo', height=280, color='Tipo de Gol')
    fig_barra.update_layout(margin=dict(l=20, r=20, t=40, b=20), showlegend=False)
    st.plotly_chart(fig_barra, use_container_width=True)

# Gráfico 3: Dispersão (Minuto do gol vs Data da partida)
with col3:
    df_scatter = df_filtrado.dropna(subset=['goal_minute'])
    fig_disp = px.scatter(df_scatter, x='date', y='goal_minute', color='venue', 
                          title='🎯 Dispersão: Minuto do Gol vs Data (Por Mando)', height=280)
    fig_disp.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_disp, use_container_width=True)

# Gráfico 4: Pizza (Proporção de gols Casa vs Fora)
with col4:
    gols_local = df_filtrado['venue'].value_counts().reset_index()
    gols_local.columns = ['Local', 'Quantidade']
    fig_pizza = px.pie(gols_local, names='Local', values='Quantidade', title='🍕 Gols: Casa vs Fora', height=280, hole=0.4)
    fig_pizza.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_pizza, use_container_width=True)