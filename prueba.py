import sqlite3

conn = sqlite3.connect("dialogos.db")
c = conn.cursor()

c.execute("PRAGMA table_info(dialogos)")

for columna in c.fetchall():
    print(columna)

conn.close()