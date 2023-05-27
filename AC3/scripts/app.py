import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px

# Titulo da aplicação, base de dados, setores, variaveis e funções
st.write(
    """
    **Fundos imobiliários**
    """
)

st.sidebar.header("Escolha as categorias")


def get_data():
    path = "../bases tratadas/funds.csv"
    return pd.read_csv(path, sep=",", header=0)


df = get_data()

variacoes = {
    "Positiva": "Fundos com variação de preço positiva",
    "Negativa": "Fundos com variação de preço negativa",
    "Todos": "Todos os fundos",
}

setores = ["Todos"] + df["sector"].drop_duplicates().tolist()

escolha_da_variacao_de_preco = st.sidebar.checkbox("Variação de preço")

escolha_de_comparacoes_de_setores = st.sidebar.checkbox("Comparações de setores")

if escolha_da_variacao_de_preco:
    tipo_de_variacao = st.sidebar.selectbox(
        "Escolha o tipo de variação", list(variacoes.keys())
    )

    setor = st.sidebar.selectbox("Escolha o setor", setores)
    dividendo_versus_preco = st.sidebar.checkbox("Dividendo v. Preço")

    st.header(
        variacoes[tipo_de_variacao]
        + (f" do setor '{setor}'" if setor != "Todos" else " de todos os setores")
    )

    if setor == "Todos" and tipo_de_variacao == "Positiva":
        data = df[df["priceVariation"] > 0]
    elif setor == "Todos" and tipo_de_variacao == "Negativa":
        data = df[df["priceVariation"] < 0]
    elif setor == "Todos" and tipo_de_variacao == "Todos":
        data = df
    elif setor != "Todos" and tipo_de_variacao == "Positiva":
        data = df[(df["sector"] == setor) & (df["priceVariation"] > 0)]
    elif setor != "Todos" and tipo_de_variacao == "Negativa":
        data = df[(df["sector"] == setor) & (df["priceVariation"] < 0)]
    elif setor != "Todos" and tipo_de_variacao == "Todos":
        data = df[df["sector"] == setor]

    # Grafico de linha
    st.line_chart(
        data=data,
        x="priceVariation",
        y="currentPrice",
        width=0,
        height=0,
    )

    if dividendo_versus_preco:
        st.header("Dividendo v. Preço")

        st.write("Dividendo v. Preço para os fundos selecionados com base nos setores selecionados")

        # Grafico de dispersão

        fig = px.scatter(
            data_frame=data,
            x="currentPrice",
            y="dividend",
            hover_name="code",
            size="dividend",
            color="dividend",
        )

        st.plotly_chart(fig)


if escolha_de_comparacoes_de_setores:
    st.header("Comparação de setores")

    st.write("Comparação de setores com o preço atual")

    escolha_de_setores = st.sidebar.multiselect("Escolha os setores", setores[1:])

    gerar_histograma_de_dividendo = st.sidebar.checkbox("Gerar histograma de dividendo")

    # Grafico de barras verticais
    st.bar_chart(
        data=df[df["sector"].isin(escolha_de_setores)]
        if len(escolha_de_setores) > 0
        else df,
        x="sector",
        y="currentPrice",
    )

    if gerar_histograma_de_dividendo:
        st.header("Histograma de dividendo")
        
        # Histograma
        fig = px.histogram(
            data_frame=df[df["sector"].isin(escolha_de_setores)]
            if len(escolha_de_setores) > 0
            else df,
            x="dividend",
        )

        st.plotly_chart(fig)

    data = (
        df[df["sector"].isin(escolha_de_setores)] if len(escolha_de_setores) > 0 else df
    )

    data = data.groupby("sector").mean().reset_index()

    # Grafico de pizza
    fig = px.pie(
        data_frame=data,
        names="sector",
        values="dailyLiquidity",
        title="Liquidez diária média por setor",
    )
    
    st.plotly_chart(fig)

    data = (
        df[df["sector"].isin(escolha_de_setores)] if len(escolha_de_setores) > 0 else df
    )

    data = data.groupby("sector").count().reset_index()

    # Grafico de barras horizontais
    fig = px.bar(
        data_frame=data,
        x="code",
        y="sector",
        orientation="h",
        title="Quantidade de fundos por setor",
    )

    st.plotly_chart(fig)
