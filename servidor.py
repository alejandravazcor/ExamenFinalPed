#!/usr/bin/env python3
import socket
import sys
import threading
from protocolo import PUERTO, ENCODING, cargar_fichero, contar_lineas_fichero, generar_respuesta

def atender_cliente(conexion, direccion, frases, total_lineas):
    with conexion:
        try:
            datos = b""
            while b"\n" not in datos:
                trozo = conexion.recv(1024)
                if not trozo:
                    break
                datos += trozo
            comando = datos.decode(ENCODING).strip()
            print(f"{direccion[0]} {comando}", file=sys.stderr)
            respuesta = generar_respuesta(comando, frases, total_lineas)
            conexion.sendall(respuesta.encode(ENCODING))
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)

def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <fichero_frases>", file=sys.stderr)
        sys.exit(1)
    frases = cargar_fichero(sys.argv[1])
    total_lineas = contar_lineas_fichero(sys.argv[1])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("", PUERTO))
        srv.listen()
        print(f"Escuchando en {PUERTO}...")
        while True:
            conn, addr = srv.accept()
            threading.Thread(target=atender_cliente,
                             args=(conn, addr, frases, total_lineas),
                             daemon=True).start()

if __name__ == "__main__":
    main()
