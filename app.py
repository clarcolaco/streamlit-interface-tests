import streamlit as st
### tabelas
#### usando pandinhas
import pandas as pd
import numpy as np
    # primeira linha registros
    # segunda linha titulos

df = pd.DataFrame(
    np.random.rand(10, 3),
    columns=['Preco', 'Taxa de ocupacao', 'Taxa de inadimplencia']
)

st.markdown("# Meu site")
st.markdown("##### Seja bem vindo :)")
st.sidebar.header("Sidebar")
st.sidebar.text("Clique em algum botao para mais")

#### criando botoes
if st.sidebar.button("Abrir tabelas"):
    st.table(df)
    st.dataframe(df)

if st.sidebar.button("Abrir gráficos"):
    st.line_chart(df)
    st.bar_chart(df)

if st.sidebar.button("Saber informacoes"):    
    st.text("teste subtitulo") 
    st.markdown("Meu título")
    st.markdown("# Meu título")
    st.markdown("˜˜Meu título˜˜")

    st.caption("Minha legenda")

    pessoas = [ {'Nome': 'Clarissa', 'Signo':'Peixes'},
                {'Nome':'Teste', 'Signo':'Teste'}]

    ### printa qualquer coisa generica! :)
    st.write("# Pessoas", pessoas)

st.sidebar.text("Clar @ 2023")