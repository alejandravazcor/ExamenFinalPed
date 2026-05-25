import random

PUERTO = 11000 + 10 * 3   # 11030
ENCODING = "utf-8"

def generar_respuesta(comando, frases, total_lineas):
    cmd = comando.strip()
    if cmd == "frase":
        return "frase " + random.choice(frases)
    return "error"
