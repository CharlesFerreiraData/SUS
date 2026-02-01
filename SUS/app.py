import streamlit as st
import pandas as pd

st.title("💊 Consulta de Remédios Rio")

try:
    # Lê a base final
    df = pd.read_csv('data/gold/base_consulta.csv')
    
    busca = st.text_input("Qual remédio você procura?")
    
    if busca:
        resultado = df[df['medicamento'].str.contains(busca.upper(), na=False)]
        
        if not resultado.empty:
            for index, linha in resultado.iterrows():
                # O ERRO ACONTECE AQUI: linha['unidade'] deve existir no CSV
                with st.expander(f"📍 {linha['unidade']}"):
                    st.write(f"🏠 **Endereço:** {linha['endereco']}")
                    st.write(f"📄 **Requisitos:** {linha['requisitos']}")
        else:
            st.warning("Não encontrado.")
except Exception as e:
    st.error(f"Erro: {e}. Verifique se o pipeline.py foi rodado.")