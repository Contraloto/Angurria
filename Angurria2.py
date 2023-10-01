import streamlit as st
import random
import smtplib
from email.mime.text import MIMEText

# Diccionario para almacenar las salas y sus códigos
salas = {}

# Título de la aplicación
st.title("Sala de Chat")

# Selección de acción: Crear sala o unirse a sala
accion = st.radio("Selecciona una acción:", ("Crear una sala", "Unirse a una sala"))

if accion == "Crear una sala":
    sala_id = st.text_input("Ingresa un nombre para la sala:")
    email = st.text_input("Ingresa tu dirección de correo electrónico:")
    
    if st.button("Crear Sala"):
        if sala_id and email:
            codigo_sala = random.randint(1000, 9999)  # Genera un código de 4 dígitos
            codigo_sala = str(codigo_sala)
            salas[codigo_sala] = {"nombre_sala": sala_id, "mensajes": []}
            st.balloons()
            st.success(f"Sala '{sala_id}' creada con éxito. Código de sala: {codigo_sala}")
            
            # Envío de correo electrónico
            try:
                server = smtplib.SMTP('smtp.example.com', 587)  # Reemplaza con tu servidor SMTP
                server.starttls()
                server.login('tucorreo@example.com', 'tucontraseña')  # Reemplaza con tus credenciales
                message = MIMEText(f"Tu código de sala es: {codigo_sala}")
                message['From'] = 'tucorreo@example.com'  # Reemplaza con tu dirección de correo
                message['To'] = email
                message['Subject'] = 'Código de sala'
                server.sendmail('tucorreo@example.com', email, message.as_string())
                server.quit()
                st.success(f"Correo electrónico enviado a {email} con el código de la sala.")
            except Exception as e:
                st.error(f"Error al enviar el correo electrónico: {e}")

elif accion == "Unirse a una sala":
    codigo_ingresado = st.text_input("Ingresa el código de la sala:")
    if st.button("Unirse a Sala"):
        if codigo_ingresado:
            if codigo_ingresado in salas:
                st.balloons()
                st.success(f"Te has unido a la sala '{salas[codigo_ingresado]['nombre_sala']}'")
            else:
                st.error("Código de sala no válido. Inténtalo de nuevo.")

# Chat en la sala (puede ser mejorado para incluir más características)
if accion == "Unirse a una sala" and codigo_ingresado in salas:
    sala_actual = salas[codigo_ingresado]
    mensaje = st.text_area("Escribe un mensaje:")
    if st.button("Enviar"):
        if mensaje:
            sala_actual["mensajes"].append(f"Usuario: {mensaje}")




