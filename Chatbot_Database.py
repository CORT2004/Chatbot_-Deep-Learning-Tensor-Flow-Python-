import sqlite3
import json

# Crear/conectar a la base de datos
conn = sqlite3.connect("dialogos.db")
c = conn.cursor()

# Eliminar tabla si ya existe
c.execute("DROP TABLE IF EXISTS dialogos")

# Crear tabla
c.execute("""
CREATE TABLE dialogos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conversacion INTEGER,
    orden INTEGER,
    texto TEXT
)
""")

# Leer archivo JSONL
with open(
    r"C:/Users/riost/OneDrive/Desktop/Proyecto IA/Base de datos/0/1956972100.jsonl",
    "r",
    encoding="utf-8"
) as f:

    num_conversacion = 1

    for linea in f:

        linea = linea.strip()

        if not linea:
            continue

        registro = json.loads(linea)

        dialogos = registro.get("dialogues", [])

        for orden, texto in enumerate(dialogos):

            c.execute("""
                INSERT INTO dialogos
                (conversacion, orden, texto)
                VALUES (?, ?, ?)
            """, (num_conversacion, orden, texto))

        num_conversacion += 1

conn.commit()
conn.close()

print("Base de datos creada correctamente.")