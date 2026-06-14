import joblib
from sklearn.metrics.pairwise import cosine_similarity

print("Cargando chatbot...")

vectorizer = joblib.load("vectorizer.pkl")
tfidf_matrix = joblib.load("tfidf_matrix.pkl")
datos = joblib.load("datos.pkl")

print("Chatbot listo")
print("Escribe 'salir' para terminar")

while True:

    pregunta = input("\nTú: ")

    if pregunta.lower() == "salir":
        break

    pregunta_vector = vectorizer.transform([pregunta])

    similitudes = cosine_similarity(
        pregunta_vector,
        tfidf_matrix
    )

    indice = similitudes.argmax()

    respuesta = datos.iloc[indice]["respuesta"]

    print("Bot:", respuesta)