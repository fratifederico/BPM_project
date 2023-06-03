import openai
import pandas as pd

# Carica il dataset dei prodotti Amazon
dataset = pd.read_csv("../csv/amazon_laptops.csv")

# Rimuovi le colonne specifiche
colonne_da_rimuovere = ["rating_count", "url"]

# sovrascrivo direttamente il dataset originale
dataset.drop(columns=colonne_da_rimuovere, inplace=True)

# Prendi una riga casuale dal dataset
riga_casuale = dataset.sample(n=1)

riga_casuale.to_csv("random_row.txt", sep="\t", index=False)

# Costruisci il prompt utilizzando i valori estratti

prompt = "riesci a scrivere una user guide più completa possibile per il seguente prodotto? Restituisci " \
         "esclusivamente la user guide. Assicurati di includere informazioni sulle caratteristiche del prodotto, " \
         "le specifiche tecniche, le istruzioni per l'uso e la manutenzione, e qualsiasi altra informazione rilevante " \
         "che potrebbe essere utile per i potenziali acquirenti. Fornisci anche consigli su come godere al meglio del " \
         "prodotto e affrontare eventuali problemi comuni o domande frequenti. L'obiettivo è fornire una guida chiara " \
         "e completa che soddisfi le esigenze e le aspettative dei clienti interessati a questo prodotto. Cerca di " \
         "fornire anche dei modi creativi per utilizzare il prodotto, non per forza suggeriti dal dataset. Prediligi " \
         "comunque la chiarezza di esposizione ed evita di essere eccessivamente ripetitivo. Ti mando una row presa " \
         "da un dataset di prodotti amazon, con relative intestazioni:\n\n" + riga_casuale.to_string(
    index=False)

openai.api_key = "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"

# Chiamata all'API di OpenAI utilizzando il prompt
risposta = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
    temperature=0.9
)

# Estrai la risposta dall'output
output = risposta.choices[0].message.content

# Salvataggio dell'output in un file di testo
with open("../output/user_guide.txt", "w") as file:
    file.write(output)

print("User guide generata e salvata nel file 'user_guide.txt'")

# valutazione delle user guide

prompt = "Con le seguenti specifiche di prodotto, come valuteresti con un voto da 0 a 100 (rispondi solo col numero, senza nemmeno la punteggiatura) " \
         "la user guide che si trova in fondo al prompt (dopo il tag USER GUIDE)?:" + riga_casuale.to_string(index=False) + "\nUSER GUIDE: " + output


# Chiamata all'API di OpenAI utilizzando il prompt
risposta = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

# Estrai la risposta dall'output
output = risposta.choices[0].message.content

# Salvataggio dell'output in un file di testo
with open("../output/score_user_guide.txt", "w") as file:
    file.write(output)

print("User guide salvata in un txt")

riga_casuale = riga_casuale.to_string(index=False, header=False)
print(riga_casuale)

# generazione da parte di gpt per il prompt ottimale per DALL-E
prompt = "utilizzando le specifiche dopo i due punti, scrivi un prompt adeguato per la generazione di un " \
         "immagine relativa allo stesso per DALL-E. Preferisci la chiarezza dell'immagine, che deve essere più " \
         "attinente possibile alle specifiche fornite. Rispondi fornendo solo il prompt :"+riga_casuale

risposta = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)
output = risposta.choices[0].message.content

response = openai.Image.create(
    prompt=output,
    n=1,
    size="1024x1024"
)

print("url to the generated image:")
print(response["data"][0]["url"])

