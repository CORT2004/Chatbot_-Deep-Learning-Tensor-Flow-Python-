import sqlite3

conn = sqlite3.connect("dialogos.db")
c = conn.cursor()

with open("train.from", "w", encoding="utf8") as f_from, \
     open("train.to", "w", encoding="utf8") as f_to, \
     open("test.from", "w", encoding="utf8") as test_from, \
     open("test.to", "w", encoding="utf8") as test_to:

    conversaciones = c.execute("""
        SELECT DISTINCT conversacion
        FROM dialogos
        ORDER BY conversacion
    """).fetchall()

    primera_conversacion = True

    for conv in conversaciones:

        conv_id = conv[0]

        filas = c.execute("""
            SELECT texto
            FROM dialogos
            WHERE conversacion = ?
            ORDER BY orden
        """, (conv_id,)).fetchall()

        textos = [fila[0].strip() for fila in filas]

        if len(textos) < 2:
            continue

        for i in range(len(textos) - 1):

            entrada = textos[i]
            salida = textos[i + 1]

            if primera_conversacion:
                test_from.write(entrada + "\n")
                test_to.write(salida + "\n")
            else:
                f_from.write(entrada + "\n")
                f_to.write(salida + "\n")

        primera_conversacion = False

conn.close()

print("Archivos de entrenamiento generados.")