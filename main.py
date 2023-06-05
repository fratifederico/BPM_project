import binascii
import openai
from image_generation import image_generation
from user_guide_generation import user_guide_generation
from user_guide_score import user_guide_score
import time
from pdf_generation import pdf_generation
from text_extraction_from_PDF import extract_text_from_pdf
from word_count import word_count
import pandas as pd
import os
from cosine_similarity import calculate_cosine_similarity
from rank_parole import plot_rank_parole

openai.api_key = "insert api key here"

dataset = pd.read_csv("processed_dataset/random_sampled_dataset.csv")

i = 0
numero_iterazioni = 20

if i == 0:
    # pulisco i file con gli score delle guide utente
    if os.path.exists("output/score_user_guide.txt"):
        # Elimina il file
        os.remove("output/score_user_guide.txt")

    # pulisco i file con gli score delle guide utente
    if os.path.exists("output/grafici/cosine_similarity.txt"):
        # Elimina il file
        os.remove("output/grafici/cosine_similarity.txt")

    # pulisco i file con gli score delle guide utente
    if os.path.exists("output/grafici/word_count.csv"):
        # Elimina il file
        os.remove("output/grafici/word_count.csv")

    # pulisco i file con gli score delle guide utente
    if os.path.exists("output/grafici/rank_parole.txt"):
        # Elimina il file
        os.remove("output/grafici/rank_parole.txt")

    if os.path.exists("output/score_user_guide.txt"):
        # Elimina il file
        os.remove("output/score_user_guide.txt")

while i <= numero_iterazioni:
    try:
        print("iteration: " + str(i) + "\n")
        actual_line = dataset.iloc[i]
        generated_user_guide = user_guide_generation(actual_line)
        time.sleep(10)
        real_user_guide = extract_text_from_pdf("real_user_guides_pdf/" + str(i) + ".pdf")
        # generazione di un immagine con DALL-E e si recupera anche la real image del prodotto
        time.sleep(30)
        image_generation(actual_line)
        time.sleep(30)
        pdf_generation(i)
        score = user_guide_score(actual_line, generated_user_guide)

        # aggiorno i file coi valori per generare i grafici:
        # word count
        conteggio_real_user_guide = word_count(real_user_guide)
        conteggio_generated_user_guide = word_count(generated_user_guide)
        with open("output/grafici/word_count.csv", "a") as file:
            file.write(str(conteggio_real_user_guide) + "," + str(conteggio_generated_user_guide) + "\n")

        # cosine sim
        cosine_similarity = calculate_cosine_similarity(real_user_guide, generated_user_guide)
        with open("output/grafici/cosine_similarity.txt", "a") as file:
            file.write(str(cosine_similarity) + "\n")

        # rank parole
        plot_rank_parole(real_user_guide, generated_user_guide, 10, i)
        i = i + 1
    except binascii.Error as e:
        print("errore di padding incorretto nella pdf generation")
        continue


# prendo un sample del dataset
random_row = dataset.sample(n=1)
random_row.to_csv("output/random_row.txt", sep="\t", index=False)

# creazione user_guide
user_guide = user_guide_generation(random_row)

# valutazione delle user guide

# attesa di 3 secondi per evitare "RateLimitError" di openai
time.sleep(3)
score = user_guide_score(random_row, user_guide)

testo_estratto = extract_text_from_pdf("path_guida_reale.pdf");


# generazione di un immagine con DALL-E

time.sleep(10)
image_url = image_generation(random_row)

#genero il pdf
time.sleep(3)
pdf_generation()

