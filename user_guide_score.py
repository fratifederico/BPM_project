import openai


def user_guide_score(random_row, user_guide):
    """
        Calcola il punteggio di valutazione della user guide utilizzando l'API di OpenAI.

        Args:
            random_row (pd.Series): Una riga casuale con le specifiche di prodotto.
            user_guide (str): La user guide da valutare.

        Returns:
            str: Il punteggio di valutazione della user guide.

        """

    prompt = "Con le seguenti specifiche di prodotto, come valuteresti con un voto da 0 a 100 (esprimi il risultato SOLO in numeri, " \
             "senza punteggiatura, e NON considerare il fatto che le immagini non siano presenti " \
             "nel voto espresso) la user guide che si trova in fondo al prompt (dopo il tag USER " \
             "GUIDE)?:" + random_row.to_string(index=False) + "\nUSER GUIDE: " + user_guide

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
    with open("output/score_user_guide.txt", "a") as file:
        file.write(output+"\n")

    print("Score della user guide salvato nel txt score_user_guide. Voto: "+output)
    return output
