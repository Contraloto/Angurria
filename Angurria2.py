import streamlit as st

# Página principal
st.title("Página Principal")
st.image("", caption="Imagen de ejemplo")

if st.button("Ir a la otra página"):
    st.write("Redirigiendo a la otra página...")
    # Redirigir al usuario a otra página
    st.experimental_set_query_params(pagina="otra")
