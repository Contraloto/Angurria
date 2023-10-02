import streamlit as st

# Página inicial
st.title("Página Inicial")
opcion = st.selectbox("Selecciona una opción:", ("Página 1", "Página 2"))

if opcion == "Página 1":
    # Contenido de la página 1
    st.header("Página 1")
    st.write("Este es el contenido de la página 1.")
elif opcion == "Página 2":
    # Contenido de la página 2
    st.header("Página 2")
    st.write("Este es el contenido de la página 2.")



