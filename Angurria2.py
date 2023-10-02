import streamlit as st
import random

# Diccionario para almacenar las salas y sus códigos
salas = {}

# Título de la aplicación
st.title("Sala de Chat")

# Selección de acción: Crear sala o unirse a sala
accion = st.radio("Selecciona una acción:", ("Crear una sala", "Unirse a una sala"))

if accion == "Crear una sala":
    sala_id = st.text_input("Ingresa un nombre para la sala:")
    
    if st.button("Crear Sala"):
        if sala_id:
            codigo_sala = random.randint(1000, 9999)  # Genera un código de 4 dígitos
            codigo_sala = str(codigo_sala)
            salas[codigo_sala] = {"nombre_sala": sala_id, "mensajes": []}
            
            # Ventana emergente de bienvenida
            st.balloons()
            st.write(f"Bienvenido a la Sala '{sala_id}'")
            st.write(f"Tu código de sala es: {codigo_sala}")

elif accion == "Unirse a una sala":
    codigo_ingresado = st.text_input("Ingresa el código de la sala:")
    if st.button("Unirse a Sala"):
        if codigo_ingresado in salas:
            st.balloons()
            st.success(f"Te has unido a la sala '{salas[codigo_ingresado]['nombre_sala']}'")

# Chat en la sala (puede ser mejorado para incluir más características)
if accion == "Unirse a una sala" and codigo_ingresado in salas:
    sala_actual = salas[codigo_ingresado]
    mensaje = st.text_area("Escribe un mensaje:")
    if st.button("Enviar"):
        if mensaje:
            sala_actual["mensajes"].append(f"Usuario: {mensaje}")


