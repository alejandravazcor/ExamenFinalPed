#!/usr/bin/env python3
import socket
import sys
from protocolo import PUERTO, construir_mensaje, decodificar_respuesta

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
    host = input("Direccion del servidor: ").strip()
    print(f"Conectando a {host}:{PUERTO}")
    for cmd in MENSAJES:
        print(f"Enviando: {cmd}")
        try:
            respuesta = enviar_comando(host, PUERTO, cmd)
            print(f"Respuesta: {respuesta}")
        except Exception as e:
            print(f"Error: no se pudo conectar con {host}:{PUERTO} - {e}", file=sys.stderr)
            sys.exit(1)
    print("Desconectado.")

if __name__ == "__main__":
    main()
