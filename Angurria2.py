import streamlit as st
import random
import time

# Diccionario para almacenar las salas y sus códigos
salas = {}

# Título de la aplicación
st.title("Sala de Chat")

# Agrega el CSS personalizado
st.markdown(
    '<link rel="stylesheet" href="css/custom.css">',
    unsafe_allow_html=True
)

# Selección de acción: Crear sala o unirse a sala
accion = st.radio("Selecciona una acción:", ("Crear una sala", "Unirse a una sala"))

if accion == "Crear una sala":
    sala_id = st.text_input("Ingresa un nombre para la sala:")
    if st.button("Crear Sala"):
        if sala_id:
            codigo_sala = str(hash(sala_id))
            salas[codigo_sala] = {"nombre_sala": sala_id, "mensajes": []}
            st.balloons()
            st.success(f"Sala '{sala_id}' creada con éxito. Código de sala: {codigo_sala}")
            
            # Agrega un retraso de 5 segundos
            with st.empty():
                for i in range(5):
                    st.progress(i / 5)
                    time.sleep(1)
                st.empty()  # Borra la barra de progreso
                
                # Redirecciona a una nueva página
                st.experimental_rerun()
            
elif accion == "Unirse a una sala":
    codigo_ingresado = st.text_input("Ingresa el código de la sala:")
    if st.button("Unirse a Sala"):
        if codigo_ingresado in salas:
            st.balloons()
            st.success(f"Te has unido a la sala '{salas[codigo_ingresado]['nombre_sala']}'")
            # Agrega aquí la redirección a una nueva página para solicitar el nombre y avatar.

# Chat en la sala (puede ser mejorado para incluir más características)
if accion == "Unirse a una sala" and codigo_ingresado in salas:
    sala_actual = salas[codigo_ingresado]
    mensaje = st.text_area("Escribe un mensaje:")
    if st.button("Enviar"):
        if mensaje:
            sala_actual["mensajes"].append(f"Usuario: {mensaje}")



