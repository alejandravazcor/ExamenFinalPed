import random

PUERTO = 11000 + 10 * 3   # 11030
ENCODING = "utf-8"

def cargar_fichero(ruta):
    with open(ruta, encoding=ENCODING) as f:
        contenido = f.read()
    bloques = [b.strip() for b in contenido.split("\n%\n") if b.strip()]
    return bloques

def contar_lineas_fichero(ruta):
    with open(ruta, encoding=ENCODING) as f:
        return sum(1 for _ in f)

def generar_respuesta(comando, frases, total_lineas):
    cmd = comando.strip()
    if cmd == "frase":
        return "frase " + random.choice(frases)
    if cmd == "total":
        return f"{len(frases)} FRASES {total_lineas} LINEAS"
    return "error"

def construir_mensaje(comando):
    return (comando + "\n").encode(ENCODING)

def decodificar_respuesta(datos):
    return datos.decode(ENCODING).strip()
