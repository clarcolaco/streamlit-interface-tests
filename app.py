import streamlit as st

st.header("testando o titulo!")
st.text("teste subtitulo")
st.sidebar.header("Titulo")
st.sidebar.text("Meu sidebar")


st.markdown("Meu título")
st.markdown("# Meu título")
st.markdown("˜˜Meu título˜˜")

st.caption("Minha legenda")

pessoas = [ {'Nome': 'Clarissa', 'Signo':'Peixes'},
            {'Nome':'Teste', 'Signo':'Teste'}]

### printa qualquer coisa generica! :)
st.write("# Pessoas", pessoas)

### tabelas
#### usando pandinhas
import pandas as pd
import numpy as np
    # primeira linha registros
    # segunda linha tiulos
df = pd.DataFrame(
    np.random.rand(10, 3),
    columns=['Preco', 'Taxa de ocupacao', 'Taxa de inadimplencia']
)

st.table(df)
st.dataframe(df)
st.line_chart(df)
st.bar_chart(df)