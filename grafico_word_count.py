import matplotlib.pyplot as plt
import numpy as np


def confronta_istogramma(array1, array2):
    # Verifica se gli array hanno la stessa lunghezza
    if len(array1) != len(array2):
        print("Gli array devono avere la stessa lunghezza.")
        return

    # Crea un array di indici per l'asse x
    indici = np.arange(len(array1))

    # Crea il grafico a barre dell'istogramma
    larghezza_barre = 0.35
    fig, ax = plt.subplots()
    barre1 = ax.bar(indici, array1, larghezza_barre, label='Array 1')
    barre2 = ax.bar(indici + larghezza_barre, array2, larghezza_barre, label='Array 2')

    # Aggiungi etichette, titolo e legenda al grafico
    ax.set_xlabel('Posizione')
    ax.set_ylabel('Valore')
    ax.set_title('Confronto valori tra Array 1 e Array 2')
    ax.set_xticks(indici + larghezza_barre / 2)
    ax.set_xticklabels(indici)
    ax.legend()

    # Mostra il grafico
    plt.show()


# Esempio di utilizzo
array1 = [10, 25, 15, 30, 20]
array2 = [5, 20, 10, 15, 25]
confronta_istogramma(array1, array2)
