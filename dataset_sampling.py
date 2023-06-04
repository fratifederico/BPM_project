import pandas as pd


def random_sampling(numero_campioni):
    """
    Estrare un campione dal dataset
        args:
            numero di campioni da prelevare dal dataset
        return:
            nulla, salva il dataset in ./processed_dataset/random_sampled_dataset.csv

    """
    path = "processed_dataset/flipkart_dataset.csv"
    # Esempio di utilizzo
    dataset_originale = pd.read_csv(path)

    campioni_prelevati = dataset_originale.sample(numero_campioni)

    # Reimpostazione degli indici
    campioni_prelevati = campioni_prelevati.reset_index(drop=True)

    # Creazione del nuovo dataset con i campioni prelevati
    campioni_prelevati.to_csv("processed_dataset/random_sampled_dataset.csv")


random_sampling(40)

# Carica il dataset
df = pd.read_csv("processed_dataset/random_sampled_dataset.csv")

# Seleziona le righe desiderate
righe_selezionate = df.iloc[list(range(19)) + [23, 24, 28, 32, 35, 39, 42]]
righe_selezionate = righe_selezionate.reset_index(drop=True)
righe_selezionate.drop("Unnamed: 0", inplace=True, axis=1)

# Salva le righe selezionate in un nuovo DataFrame o file CSV
righe_selezionate.to_csv("processed_dataset/random_sampled_dataset.csv")

