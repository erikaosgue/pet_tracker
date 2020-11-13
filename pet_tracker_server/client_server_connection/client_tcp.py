#!/usr/bin/python3
from socket import create_connection

# Conectar al servidor.
with create_connection(("localhost", 6190)) as conn:
    print("Conectado al servidor.")
    # Enviar datos.
    conn.sendall(b"Hola mundo!")

print("Conexión cerrada.")
