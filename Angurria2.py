import streamlit as st
import random

# Diccionario para almacenar las salas y sus códigos
salas = {}

# Título de la aplicación
st.title("Sala de Chat")

# Selección de acción: Crear sala o unirse a sala
accion = st.radio("Selecciona una acción:", ("Crear una sala", "Unirse a una sala"))

if accion == "Crear una sala":
    # Genera un código de sala aleatorio
    codigo_sala = random.randint(1000, 9999)
    st.write(f"Tu código de sala es: {codigo_sala}")
    sala_id = st.text_input("Ingresa un nombre para la sala:")
    if st.button("Crear Sala"):
        if sala_id:
            salas[codigo_sala] = {"nombre_sala": sala_id, "mensajes": []}
            st.success(f"Sala '{sala_id}' creada con éxito.")

elif accion == "Unirse a una sala":
    codigo_ingresado = st.text_input("Ingresa el código de la sala:")
    if st.button("Unirse a Sala"):
        if codigo_ingresado:
            if int(codigo_ingresado) in salas:
                sala_actual = salas[int(codigo_ingresado)]
                st.write(f"Te has unido a la sala '{sala_actual['nombre_sala']}'")
                st.write(f"Código de sala: {codigo_ingresado}")
                st.write("Mensajes en la sala:")
                mensajes_sala = sala_actual["mensajes"]
                for mensaje in mensajes_sala:
                    st.write(mensaje)
            else:
                st.error("Código de sala no válido. Inténtalo de nuevo.")

# Chat en la sala (puede ser mejorado para incluir más características)
mensaje = st.text_area("Escribe un mensaje:")
if st.button("Enviar"):
    if accion == "Unirse a una sala" and int(codigo_ingresado) in salas:
        sala_actual["mensajes"].append(f"Usuario: {mensaje}")

