import streamlit as st

# Diccionario para almacenar las salas y los códigos de sala
salas = {}

def crear_sala():
    codigo_sala = st.text_input("Ingresa un código para la sala:")
    if codigo_sala:
        salas[codigo_sala] = []
        st.write(f"Sala creada con código: {codigo_sala}")
        st.write("Esperando a que otros se unan a la sala...")

def unirse_a_sala():
    codigo_sala = st.text_input("Ingresa el código de la sala:")
    if codigo_sala in salas:
        salas[codigo_sala].append(st.text_input("Ingresa tu nombre:"))
        st.write(f"Te has unido a la sala {codigo_sala}")
        st.write("Participantes en la sala:")
        st.write(salas[codigo_sala])
    else:
        st.write("Código de sala incorrecto. Inténtalo de nuevo.")

# Página principal
st.title("Sala de Espera")

opcion = st.selectbox("Selecciona una opción:", ["Crear una sala", "Unirse a una sala"])

if opcion == "Crear una sala":
    crear_sala()
elif opcion == "Unirse a una sala":
    unirse_a_sala()