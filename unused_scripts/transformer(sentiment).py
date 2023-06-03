from transformers import pipeline

# Crea il sentiment analysis pipeline
sentiment_classifier = pipeline("sentiment-analysis")

# Definisci il prompt
prompt = ""
# Esegui il sentiment analysis sul prompt
sentiment = sentiment_classifier(prompt)

# Estrai il valore del sentiment e la sua etichetta
sentiment_label = sentiment[0]["label"]
sentiment_score = sentiment[0]["score"]

# Stampa i risultati
print(f"Sentiment: {sentiment_label}")
print(f"Confidenza: {sentiment_score}")
print("fine")
