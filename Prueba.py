import streamlit as st
import eventlet
import socketio

# Inicializar Streamlit
st.title("Sala de Chat en Tiempo Real")

# Inicializar Socket.IO
sio = socketio.Server()
app = socketio.WSGIApp(sio)

# Diccionario para almacenar las salas y sus códigos
salas = {}

@sio.event
def connect(sid, environ):
    st.write(f'Usuario conectado: {sid}')

def crear_sala():
    codigo_sala = st.text_input("Ingresa un código para la sala:")
    if codigo_sala:
        salas[codigo_sala] = []

        st.write(f"Sala creada con código: {codigo_sala}")
        st.write("Esperando a que otros se unan a la sala...")

def unirse_a_sala():
    codigo_sala = st.text_input("Ingresa el código de la sala:")
    if codigo_sala in salas:
        nombre = st.text_input("Ingresa tu nombre:")
        salas[codigo_sala].append(nombre)
        st.write(f"Te has unido a la sala {codigo_sala}")
        st.write("Participantes en la sala:")
        st.write(salas[codigo_sala])
    else:
        st.write("Código de sala incorrecto. Inténtalo de nuevo.")

# Página principal
st.write("Seleccione una opción:")
opcion = st.selectbox("", ["Crear una sala", "Unirse a una sala"])

if opcion == "Crear una sala":
    crear_sala()
elif opcion == "Unirse a una sala":
    unirse_a_sala()

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 8500)), app)
