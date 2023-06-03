import openai
import requests
import ast
import requests
import pandas as pd


def image_generation(random_row):
    """
        Genera un'immagine utilizzando GPT-3.5 Turbo basata su un prompt generato dalle specifiche fornite.

        Args:
            random_row (pandas.Series): Una riga casuale dal dataset di prodotti.

        Returns:
            str: L'URL all'immagine generata.
            Also saved the image into the ./output/image_dalle.jpg

        """
    random_row_string = random_row.to_string(index=False, header=False)

    # generazione da parte di gpt per il prompt ottimale per DALL-E
    prompt = "utilizzando le specifiche dopo i due punti, scrivi un prompt in inglese adeguato per la generazione di un " \
             "immagine relativa allo stesso per un tool di generazione immagini basato su intelligenza artificiale. Preferisci la chiarezza dell'immagine, che deve essere più " \
             "attinente possibile alle specifiche fornite. L'immagine deve rappresentare un prodotto, " \
             "quindi suggerisci anche di renderla accattivante, non semplicemente l'oggetto su sfondo bianco (come se " \
             "fosse un'immagine pubblicitaria) Rispondi fornendo solo il prompt, ed ometti informazioni sul prezzo. NON usare la parola 'cutting' " \
             "nel prompt :" + random_row_string

    risposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    image_prompt = risposta.choices[0].message.content

    ### problem with the 20th row of the dataset
    #print(image_prompt)
    #image_prompt = "Create an image for a beard trimmer that also has a chamber for the trimmed hair. The image should highlight the product's features and be attention-grabbing, to highlight the product features."
    ###


    response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="1024x1024"
    )

    with open("output/images_urls.txt", "a") as file:
        file.write(response["data"][0]["url"] + "\n")

    # salvo l'immagine in un file (ogni volta viene sovrascritta), in questo modo posso utlizzarla per il pdf nel caso
    image_file = requests.get(response["data"][0]["url"]).content
    with open("output/image_dalle.jpg", "wb") as f:
        f.write(image_file)

    # salvo la real image

    # Estrai la lista di URL dalla riga
    url_list = ast.literal_eval(random_row['image'])

    # Se la lista è vuota, esci
    if not url_list:
        print("Nessun URL disponibile")
        exit()

    # Seleziona il primo URL, se presente
    url = url_list[0]

    # Se il primo URL non è valido, passa al secondo URL
    if not url:
        if len(url_list) > 1:
            url = url_list[1]
        else:
            print("Nessun URL valido disponibile")
            exit()

    # Scarica l'immagine
    response = requests.get(url)
    if response.status_code == 200:
        with open("output/immagine_prodotto.jpg", "wb") as f:
            f.write(response.content)
            print("Immagine scaricata con successo")
    else:
        print("Errore nel download dell'immagine")
