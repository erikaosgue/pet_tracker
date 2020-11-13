#!/usr/bin/python3
from socket import socket

# Crear el socket.
with socket() as s:
    # Asociarlo a una dirección de IP y un puerto.
    s.bind(("10.10.255.83", 6190))
   # s.bind(("34.75.204.221", 6190))
    # Indicar que este socket actuará como servidor.
    s.listen()
    # Esperar a la conexión del cliente.
    while True:
        print("Esperando al cliente...")

        conn, address = s.accept()
        print("{}:{} se ha conectado.".format(address[0], address[1]))
        # Esperar a que el cliente envíe datos.
        while True:
            data = conn.recv(1024)
            # Chequear que no esté vacío.
            if data:
                # Imprimirlo en pantalla y cerrar el socket.
                print("El cliente ha enviado:", data)
                break

# El socket se cierra automáticamente al salir del bloque "with".
print("Conexión cerrada.")
