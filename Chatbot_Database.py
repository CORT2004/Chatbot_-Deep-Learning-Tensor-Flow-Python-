import sqlite3
import json
import glob
import sys

# LIMITE DE REGISTROS
MAX_REGISTROS = 250000

RUTA_JSON = r"C:\Users\riost\OneDrive\Desktop\Proyecto IA\Base de datos\**\*.jsonl"

conexion = sqlite3.connect("chatbot.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS dialogos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pregunta TEXT,
    respuesta TEXT
)
""")

archivos = glob.glob(RUTA_JSON, recursive=True)

print("Archivos encontrados:", len(archivos))

contador = 0

for archivo in archivos:

    try:

        with open(archivo, "r", encoding="utf8") as f:

            for linea in f:

                data = json.loads(linea)

                if "dialogues" not in data:
                    continue

                for dialogo in data["dialogues"]:

                    frases = [
                        x.strip()
                        for x in dialogo.split("\n")
                        if x.strip()
                    ]

                    for i in range(len(frases)-1):

                        pregunta = frases[i]
                        respuesta = frases[i+1]

                        cursor.execute(
                            """
                            INSERT INTO dialogos
                            (pregunta,respuesta)
                            VALUES (?,?)
                            """,
                            (pregunta,respuesta)
                        )

                        contador += 1

                        if contador % 10000 == 0:
                            conexion.commit()
                            print("Guardados:", contador)

                        if contador >= MAX_REGISTROS:

                            conexion.commit()
                            conexion.close()

                            print()
                            print("Límite alcanzado")
                            print("Total registros:", contador)

                            sys.exit()

    except Exception:
        pass

conexion.commit()
conexion.close()

print()
print("Total registros:", contador)