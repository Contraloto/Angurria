import streamlit as st

# Variable para el estado de redirección
redireccionado = False

# Página principal
st.title("Página Principal")

# Verificar si se ha redirigido a la página secundaria
if "pagina" in st.experimental_get_query_params():
    if st.experimental_get_query_params()["pagina"] == "otra":
        redireccionado = False

if redireccionado:
    st.empty()  # Limpiar la pantalla principal
    st.title("Página Secundaria")
    st.write("Bienvenido a la página secundaria")
    
    # Botón para regresar a la página principal
    if st.button("Regresar a la página principal"):
        st.experimental_set_query_params(pagina="principal")  # Redirigir de nuevo a la página principal
else:
    st.image("https://w7.pngwing.com/pngs/361/694/png-transparent-light-circle-geometry-science-and-technology-blue-mechanical-blue-angle-electronics.png", caption="Imagen de ejemplo")

    if st.button("Ir a la otra página"):
        st.write("Redirigiendo a la otra página...")
        st.experimental_set_query_params(pagina="otra")

