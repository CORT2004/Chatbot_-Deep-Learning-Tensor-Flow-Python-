import joblib

datos = joblib.load("datos.pkl")
import joblib
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = joblib.load("vectorizer.pkl")
tfidf_matrix = joblib.load("tfidf_matrix.pkl")
datos = joblib.load("datos.pkl")

pregunta = "hola"

pregunta_vector = vectorizer.transform([pregunta])

similitudes = cosine_similarity(
    pregunta_vector,
    tfidf_matrix
)

print("Forma:", similitudes.shape)
print("Mayor similitud:", similitudes.max())

indice = similitudes.argmax()

print("Indice:", indice)

print("Respuesta:")
print(datos.iloc[indice]["respuesta"])