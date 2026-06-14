import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

print("Cargando base de datos...")

conexion = sqlite3.connect("chatbot.db")

df = pd.read_sql_query(
    "SELECT pregunta, respuesta FROM dialogos",
    conexion
)

conexion.close()

print("Registros cargados:", len(df))

vectorizer = TfidfVectorizer(
    lowercase=True,
    max_features=30000,
    stop_words=None
)

print("Creando matriz TF-IDF...")

tfidf_matrix = vectorizer.fit_transform(df["pregunta"])

joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump(tfidf_matrix, "tfidf_matrix.pkl")
joblib.dump(df, "datos.pkl")

print()
print("Vectorización completada")
print("Preguntas:", len(df))
print("Vocabulario:", len(vectorizer.vocabulary_))