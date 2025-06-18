
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dados de junho de 2025
data = {
    "Produto": ["Morango", "Trigo", "Óleo de Soja", "Açúcar"],
    "Preço (R$)": [12.00, 65.32, 7.43, 63.97],
    "Data": ["2025-06-17", "2025-06-17", "2025-06-17", "2025-06-17"]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Função para gerar gráfico de tendência
def plot_trend(df, produto):
    fig, ax = plt.subplots()
    ax.plot(df["Data"], df["Preço (R$)"], marker='o')
    ax.set_title(f"Tendência de Preço - {produto}")
    ax.set_xlabel("Data")
    ax.set_ylabel("Preço (R$)")
    st.pyplot(fig)

# Título do painel
st.title("Painel de Monitoramento de Preços - Junho de 2025")

# Mostrar tabela de dados
st.subheader("Tabela de Preços")
st.write(df)

# Mostrar gráficos de tendência
for produto in df["Produto"]:
    st.subheader(f"Gráfico de Tendência - {produto}")
    plot_trend(df[df["Produto"] == produto], produto)
