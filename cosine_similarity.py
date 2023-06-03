from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from text_extraction_from_PDF import extract_text_from_pdf
import re


def normalize_text(text):
    # Rimozione dei caratteri non corretti
    cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Normalizzazione della stringa
    normalized_text = cleaned_text.lower().strip()

    # Rimozione dei caratteri di nuova riga e formattazione su una riga singola
    normalized_text = normalized_text.replace('\n', '')
    normalized_text = normalized_text.replace('\r', '')
    normalized_text = normalized_text.replace('\t', '')
    normalized_text = ' '.join(normalized_text.split())

    return normalized_text


class CustomVectorizer(TfidfVectorizer):
    def build_preprocessor(self):
        return lambda x: x


def calculate_cosine_similarity(text1, text2):
    """
       Calcola la similarità coseno tra due testi utilizzando la rappresentazione vettoriale TF-IDF.

       Args:
           text1 (str): Il primo testo da confrontare.
           text2 (str): Il secondo testo da confrontare.

       Returns:
           float: Il valore di similarità coseno tra i due testi.

       """
    # Creazione di un vettore di funzionalità TF-IDF per i testi
    vectorizer = CustomVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])

    # Calcolo della similarità coseno tra i vettori dei testi
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

    return cosine_sim[0][0]


"""
# Esempio di utilizzo
text1 = extract_text_from_pdf("official_user_guides/lenovo-ideapad-3-ideapad-slim-3-notebook-computer-manual-optimized.pdf")
with open("output/user_guide.txt", "r") as file:
    text2 = file.read()

text1 = normalize_text(text1)
text2 = normalize_text(text2)


print(text1)
print(text2)

similarity_score = calculate_cosine_similarity(text1, text2)
print(f"Similarity Score: {similarity_score}")
"""