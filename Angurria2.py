import streamlit as st
import random
import pandas as pd

rondas2 = 0
cantidad2 = 0

# Preguntar la cantidad de rondas
cantidad_rondas = st.text_input("Ingrese la cantidad de rondas:")

if cantidad_rondas.isdigit():
    rondas = int(cantidad_rondas)
    rondas2 = rondas
else:
    st.error("La cantidad debe ser un número entero. Intente nuevamente.")

# Preguntar la cantidad de jugadores
cantidad_jugadores = st.text_input("Ingrese la cantidad de jugadores:")

if cantidad_jugadores.isdigit():
    cantidad = int(cantidad_jugadores)
    cantidad2 = cantidad
else:
    st.error("La cantidad debe ser un número entero. Intente nuevamente.")

# Crear un diccionario para almacenar los datos de los jugadores
jugadores = {}

# Solicitar los nombres y otros datos de los jugadores
for i in range(cantidad2):
    nombre = st.text_input(f"Ingrese el nombre del jugador {i+1}:")

    if nombre:
        puntaje = 0
        jugadores[nombre] = puntaje

# Mostrar los datos de los jugadores
st.write("\nDatos de los jugadores:")
for nombre, datos in jugadores.items():
    st.write(nombre, datos)
st.write("Cantidad de rondas:", rondas2)

# Función para simular un lanzamiento de dado
def lanzar_dado():
    seed = random.randint(0, 1000)  # Generar una semilla aleatoria
    random.seed(seed)
    return random.randint(1, 6)  # Simulamos un dado de 6 caras

st.write("Bienvenidos Angurrias, inician los juegos del hambre")

for ronda in range(1, rondas2 + 1):
    st.write(f"Ronda {ronda}:")

    # Iterar por cada jugador
    for jugador, puntaje in jugadores.items():
        st.write(f"Turno de {jugador}:")

        while True:
            # Simular lanzamiento de dado
            valor_dado = lanzar_dado()
            st.write(f"El jugador {jugador} sacó: {valor_dado}")

            if valor_dado == 1:
                st.write(f"Eso te pasa por ANGURRIA, {jugador} pierde todos los puntos acumulados.")
                jugadores[jugador] = 0
                break
            else:
                respuesta = st.radio(f"{jugador}, ¿Seguís jugando o te da miedo?", ('si', 'no')).lower()
                if respuesta == 'si':
                    puntaje += valor_dado
                    jugadores[jugador] = puntaje
                else:
                    puntaje += valor_dado
                    jugadores[jugador] = puntaje
                    break

# Crear DataFrame con resultados
resultados = pd.DataFrame(jugadores.items(), columns=['Jugador', 'Puntaje Final'])

# Mostrar resultados
st.write("\nResultados Finales:")
st.write(resultados)
