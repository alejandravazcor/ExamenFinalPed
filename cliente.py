#!/usr/bin/env python3
import socket
from protocolo import PUERTO, construir_mensaje, decodificar_respuesta

HOST = "localhost"
MENSAJES = ["frase", "frase", "total"]

def enviar_comando(host, puerto, comando):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, puerto))
        s.sendall(construir_mensaje(comando))
        datos = b""
        while True:
            trozo = s.recv(4096)
            if not trozo:
                break
            datos += trozo
    return decodificar_respuesta(datos)

def main():
    print(f"Conectando a {HOST}:{PUERTO}")
    for cmd in MENSAJES:
        print(f"Enviando: {cmd}")
        respuesta = enviar_comando(HOST, PUERTO, cmd)
        print(f"Respuesta: {respuesta}")
    print("Desconectado.")

if __name__ == "__main__":
    main()
