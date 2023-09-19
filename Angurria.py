import random
import pandas as pd

# Preguntar la cantidad de rondas
while True:
    cantidad_rondas = input("Ingrese la cantidad de rondas: ")
    if cantidad_rondas.isdigit():
        rondas = int(cantidad_rondas)
        break
    else:
        print("La cantidad debe ser un número entero. Intente nuevamente.")

# Preguntar la cantidad de jugadores
while True:
    cantidad_jugadores = input("Ingrese la cantidad de jugadores: ")
    if cantidad_jugadores.isdigit():
        cantidad = int(cantidad_jugadores)
        break
    else:
        print("La cantidad debe ser un número entero. Intente nuevamente.")

# Crear un diccionario para almacenar los datos de los jugadores
jugadores = {}

# Solicitar los nombres y otros datos de los jugadores
for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
    puntaje = 0
    jugadores[nombre] = puntaje

# Mostrar los datos de los jugadores
print("\nDatos de los jugadores:")
for nombre, datos in jugadores.items():
    print(nombre,datos)
print("Cantidad de rondas:",rondas)

# Función para simular un lanzamiento de dado
def lanzar_dado():
    seed = random.randint(0, 1000)  # Generar una semilla aleatoria
    random.seed(seed)
    return random.randint(1, 6)  # Simulamos un dado de 6 caras

print("Bienvenidos Angurrias, inician los juegos del hambre")

for ronda in range(1, rondas + 1):
    print(f"Ronda {ronda}:")

    # Iterar por cada jugador
    for jugador, puntaje in jugadores.items():
        print(f"Turno de {jugador}:")

        while True:
            # Simular lanzamiento de dado
            valor_dado = lanzar_dado()
            print(f"El jugador {jugador} sacó: {valor_dado}")

            if valor_dado == 1:
                print(f"Eso te pasa por ANGURRIA, {jugador} pierde todos los puntos acumulados.")
                jugadores[jugador] = 0
                break
            else:
                respuesta = input(f"{jugador}, ¿Seguís jugando o te da miedo? (si/no): ").lower()
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
print("\nResultados Finales:")
print(resultados)



