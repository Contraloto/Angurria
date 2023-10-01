import streamlit as st

# Página principal
st.title("Página Principal")
st.image(r"https://w7.pngwing.com/pngs/361/694/png-transparent-light-circle-geometry-science-and-technology-blue-mechanical-blue-angle-electronics.png", caption="Imagen de ejemplo")

if st.button("Ir a la otra página"):
    st.write("Redirigiendo a la otra página...")
    # Redirigir al usuario a otra página
    st.experimental_set_query_params(pagina="otra")
