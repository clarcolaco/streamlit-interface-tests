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

if st.sidebar.checkbox("Aceito"):
    st.write("Aceito! Marcado")

### radiobuton
opcao = st.sidebar.radio("Selecione uma opcao",("Opcao 1", "Opcao 2"))
if opcao == "Opcao 1":
    st.sidebar.header("Selecionei 1")
elif opcao == "Opcao 2":
    st.sidebar.header("Selecionei 2")




###### selectbox
selectbox = st.sidebar.selectbox("Seleciona uma opcao",
("Preco", "Taxa de ocupacao"))
if selectbox == "Preco":
    st.table(df)
    st.dataframe(df)
elif selectbox == "Taxa de ocupacao":
    st.line_chart(df)
    st.bar_chart(df)


#### multiselect
opcao_mult = st.sidebar.multiselect("Selecione uma opcao",
("Preco", "Taxa"),
("Preco"))

st.sidebar.text("Clar @ 2023")