import json

ruta = r"C:/Users/riost/OneDrive/Desktop/Proyecto IA/Base de datos/0/37900.jsonl"

with open(ruta, "r", encoding="utf8") as f:
    linea = f.readline()

print(linea[:2000])