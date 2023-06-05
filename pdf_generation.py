import http.client
import base64
import json
from img_to_base64 import img_to_base64
import openai
import jwt


def pdf_generation(i):
    """
        Genera un pdf utilizzando le API di pdfgenerationapi e quelle di openAi.

        Args:
            not required

        Returns:
            nothing, it just saves the file into "./output"

        """
    conn = http.client.HTTPSConnection("us1.pdfgeneratorapi.com")

    # id value del template
    id_value = "650461"

    with open("output/user_guide.txt", 'r') as file:
        user_guide = file.read()

    with open("output/random_row.txt", 'r') as file:
        random_row = file.read()

    image1_path = "output/image_dalle.jpg"
    image2_path = "output/immagine_prodotto.jpg"
    image3_path = "output/example_images/blank_image.jpg"

    # transformo le immagini in base64 per il passaggio in json
    image1 = img_to_base64(image1_path)
    image3 = img_to_base64(image2_path)
    image2 = img_to_base64(image3_path)

    # rimuovere
    openai.api_key = "insert api key here"
    prompt = "impagina il seguente testo con dei tag html per migliorare la qualità di visualizzazione per l'utente finale (restituisci solo l'ouput atteso):\n\n" + user_guide

    # Chiamata all'API di OpenAI utilizzando il prompt
    risposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=2048
    )

    # Estrai la risposta dall'output
    user_guide = risposta.choices[0].message.content

    prompt = "Partendo dalle specifiche di prodotto in fondo a questo prompt restituisci ESCLUSIVAMENTE il nome della azienda produttrice (senza punteggiatura). Se questa non è presente, restituisci ESCLUSIVAMENTE il nome del prodotto. Rispondi esclusivamente con l'output atteso. Considera che la tua risposta verrà poi inserita in un documento professionale, quindi cerca di essere sintetico ma di inserire le informazioni rilevanti:\n\n" + random_row

    # Chiamata all'API di OpenAI utilizzando il prompt
    risposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=100
    )

    # Estrai la risposta dall'output
    footer = risposta.choices[0].message.content

    payload = {
        "id": id_value,
        "user_guide": user_guide,
        "footer": footer,
        "image1": image1,
        "image2": image2,
        "image3": image3
    }

    payload_json = json.dumps(payload)

    # parte relativa alla generazione del token JWT
    secret_key = "insert secret key from PDFgeneratorAPI here"

    # Definisci il payload del JWT
    authentication_payload = {
        "iss": "c9f1435c05e3e2a227692a3a182656c567dde43b3b0f299e9bef8036d6cc6ab1",
        "sub": "insert email here",
        "exp": 83738594538954783
    }

    # Genera il token JWT
    token = jwt.encode(authentication_payload, secret_key, algorithm='HS256')

    headers = {
        'content-type': "application/json",
        'Authorization': "Bearer " + token,
        "alg": "HS256",
        "typ": "JWT"
    }

    # chiamata post alle api di pdfgenerationapi

    conn.request("POST", "/api/v3/templates/650461/output?name=My%20document&format=pdf&output=base64",
                 payload_json, headers)
    res = conn.getresponse()
    # stampo solo se ci sono errori nella risposta
    if res.status >= 400:
        print("Errore nella richiesta:")
        print("Codice di stato:", res.status)
        print("Messaggio di errore:", res.read().decode("utf-8"))

    else:
        data = res.read()
        # Decodifica il dato base64 in byte
        pdf_data = base64.b64decode(data)

        # Salva i dati come un file PDF
        with open("output/user_guides_generated/" + str(i) + ".pdf", "wb") as file:
            file.write(pdf_data)

        print("Il PDF è stato salvato correttamente.")
