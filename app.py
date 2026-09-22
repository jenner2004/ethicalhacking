import socket
import sys

print("--- SCRIPT DE PRUEBA DE ETHICAL HACKING ---")
print(f"Versión de Python en el venv: {sys.version.split()[0]}")

# Obtener el nombre del equipo y la IP local
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"Nombre del host: {hostname}")
print(f"Tu dirección IP local es: {local_ip}")
print("---------------------------------------------")
print("¡El entorno virtual funciona a la perfección!")
