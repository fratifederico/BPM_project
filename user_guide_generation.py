import openai


def user_guide_generation(dataset_row):
    """
       Genera una user guide completa per un prodotto utilizzando l'API di OpenAI.

       Args:
           dataset_row (pd.Series): Una riga del dataset contenente le informazioni del prodotto.

       Returns:
           str: La user guide generata.

       """
    # Costruisci il prompt utilizzando i valori estratti

    ita = "in italiano"
    eng = "in inglese"
    language = eng

    prompt = "Scrivi una user guide più compelta possibile ed "+ language+ " per il prodotto che ti fornirò a fine di questo prompt. Restituisci " \
             "esclusivamente la user guide. Assicurati di includere informazioni sulle caratteristiche del prodotto, " \
             "le specifiche tecniche, le istruzioni per l'uso e la manutenzione, e qualsiasi altra informazione rilevante " \
             "che potrebbe essere utile per i potenziali acquirenti. Fornisci anche consigli su come godere al meglio del " \
             "prodotto e affrontare domande frequenti. Se hai idee per ulteriori sezioni " \
             "della user guide aggiungile pure, hai pura libertà di scelta nella generazione, ma ricorda che " \
             "l'obiettivo è fornire una guida chiara e completa che soddisfi le esigenze e le aspettative dei clienti " \
             "interessati a questo prodotto. Cerca di fornire anche dei modi creativi per utilizzare il prodotto, " \
             "non per forza suggeriti dal dataset. Non includere una formula di chiusura, in quanto questa verrà aggiunta successivamente. Ti mando una row presa da un dataset di prodotti amazon, " \
             "con relative intestazioni:\n\n" + dataset_row.to_string(index=False)

    # Chiamata all'API di OpenAI utilizzando il prompt
    risposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=3600
    )

    # Estrai la risposta dall'output
    user_guide = risposta.choices[0].message.content

    # Salvataggio dell'output in un file di testo
    with open("output/user_guide.txt", "w") as file:
        file.write(user_guide)

    # aggiunta del troubleshooting
    prompt = "Sulla base del precedente prompt, crea una lista "+language+" di possibili problemi che possono presentarsi col " \
             "prodotto, e aggiungi dopo ognuno le possibili soluzioni. Cerca di creare una guida esaustiva, ed inizia il tuo output col termine 'TROUBLESHOOTING:'," \
             " e di restituire in output esclusivamente la stessa, senza termini preliminari." \
             " Includi al termine un ringraziamento al lettore per aver scelto il prodotto e una formula di chiusura per la guida utente." \
             "Ti mando una row presa da un dataset di prodotti amazon, con relative intestazioni:\n\n" + dataset_row.to_string(index=False)

    # Chiamata all'API di OpenAI utilizzando il prompt
    risposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=3600
    )

    # Estrai la risposta dall'output
    troubleshooting = risposta.choices[0].message.content

    # salvataggio del troubleshooting
    with open("output/user_guide.txt", "a") as file:
        file.write("\n\n"+troubleshooting)

    print("User guide generata e salvata nel file 'user_guide.txt'")
    return user_guide
