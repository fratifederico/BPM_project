import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

from grafici_medie_voti_nostri import create_histogram, create_histogram_simple, create_histogram_medium, \
    create_histogram_complex


def cosine_similarity_plot():
    # Leggi i valori dal file di testo
    values = []
    with open('output/grafici/cosine_similarity.txt', 'r') as file:
        for line in file:
            value = float(line.strip())
            values.append(value)

    # Calcola media e deviazione standard
    mean = np.mean(values)
    std_dev = np.std(values)

    # Crea l'array di indici per le barre sull'asse x
    x_indices = np.arange(len(values))

    # Crea il grafico a barre
    colors = ['blue'] * len(x_indices)  # Colore predefinito per tutte le barre
    line_numbers_simple = [0, 2, 4, 9, 12, 16, 20]
    line_numbers_moderate = [6, 7, 8, 10, 15, 17, 18, 19]
    line_numbers_complex = [1, 3, 5, 11, 13, 14]
    for i in line_numbers_simple:
        colors[i] = 'blue'  # Imposta il colore giallo per gli indici semplici
    for i in line_numbers_moderate:
        colors[i] = 'orange'  # Imposta il colore rosa fluo per gli indici complessi
    for i in line_numbers_complex:
        colors[i] = 'red'  # Imposta il colore rosa fluo per gli indici complessi

    plt.bar(x_indices, values, align='center', alpha=0.5, color=colors)
    plt.xlabel('Numero di riga')
    plt.ylabel('Cosine Similarity')
    plt.title('Similarity tra due testi', fontweight='bold')
    plt.grid(True)

    # Aggiungi linee tratteggiate per la media e la deviazione standard
    plt.axhline(mean, color='r', linestyle='--', label='Media')
    plt.axhline(mean + std_dev, color='g', linestyle='--', label='Media + Dev. Std.')
    plt.axhline(mean - std_dev, color='g', linestyle='--', label='Media - Dev. Std.')
    plt.legend(fontsize='6')

    # Mostra il grafico
    plt.savefig("output/grafici/cosine_similarity_overall_plot.png")
    plt.close()


def cosine_similarity_complexity_plot(category):
    if category == "simple":
        line_numbers = [0, 2, 4, 9, 12, 16, 20]
        bar_color = "blue"
    elif category == "moderate":
        line_numbers = [6, 7, 8, 10, 15, 17, 18, 19]
        bar_color = "orange"
    elif category == "complex":
        line_numbers = [1, 3, 5, 11, 13, 14]
        bar_color = "red"
    else:
        print("ERRORE IN COSINE SIMILARITY COMPLEXITY PLOT\n")
        return

    with open('output/grafici/cosine_similarity.txt', 'r') as file:
        values = []
        # Leggi tutte le righe del file
        lines = file.readlines()

        # Estrai le righe specificate
        selected_lines = [lines[i] for i in line_numbers]

    for line in selected_lines:
        value = float(line.strip())
        values.append(value)

    # Calcola media e deviazione standard
    mean = np.mean(values)
    std_dev = np.std(values)

    # Crea l'array di identificativi delle barre sull'asse x
    x_labels = [str(i) for i in line_numbers]

    # Crea il grafico a barre
    plt.bar(x_labels, values, align='center', alpha=0.5, color=bar_color)
    plt.xlabel('Riga')
    plt.ylabel('Cosine Similarity')
    plt.title('Similarity tra due testi - Categoria: ' + category, fontweight='bold')
    plt.grid(True)

    # Aggiungi linee tratteggiate per la media e la deviazione standard
    plt.axhline(mean, color='green', linestyle='--', label='Media')
    plt.axhline(mean + std_dev, color='red', linestyle='--', label='Media + Dev. Std.')
    plt.axhline(mean - std_dev, color='red', linestyle='--', label='Media - Dev. Std.')

    # Mostra il grafico
    plt.legend(fontsize='6')
    plt.savefig("output/grafici/cosine_similarity_" + category + "_barplot.png")
    plt.close()


def word_count_plot():
    # Leggi i valori dal file di testo
    values1 = []
    values2 = []
    with open('output/grafici/word_count.csv', 'r') as file:
        for line in file:
            value1, value2 = map(int, line.strip().split(','))
            values1.append(value1)
            values2.append(value2)

    # Calcola media e deviazione standard per i primi numeri
    mean1 = np.mean(values1)
    std_dev1 = np.std(values1)

    # Calcola media e deviazione standard per i secondi numeri
    mean2 = np.mean(values2)
    std_dev2 = np.std(values2)

    # Crea l'istogramma
    index = np.arange(len(values1))
    bar_width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(index, values1, bar_width, label='Real User Guide')
    rects2 = ax.bar(index + bar_width, values2, bar_width, label='Generated User Guide')

    # Aggiungi media e deviazione standard al grafico
    ax.axhline(mean1, color='r', linestyle='--', label='Media Real User Guide')
    ax.axhline(mean1 + std_dev1, color='g', linestyle='--', label='Media + Dev. Std. Real')
    ax.axhline(mean1 - std_dev1, color='g', linestyle='--', label='Media - Dev. Std. Real')

    ax.axhline(mean2, color='m', linestyle='--', label='Media Generated User Guide')
    ax.axhline(mean2 + std_dev2, color='b', linestyle='--', label='Media + Dev. Std. Generated')
    ax.axhline(mean2 - std_dev2, color='b', linestyle='--', label='Media - Dev. Std. Generated')

    # Utilizza una scala logaritmica sull'asse delle ordinate
    ax.set_yscale('log')

    # Etichette sugli assi e titolo del grafico
    ax.set_xlabel('Product identifier')
    ax.set_ylabel('Word Count (log scale)')
    ax.set_title('Word Count tra due testi')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(range(len(values1)))

    # Mostra la legenda
    ax.legend()

    # Mostra il grafico
    plt.legend(fontsize='6')
    plt.tight_layout()
    plt.savefig("output/grafici/word_count_overall_plot.png")
    # plt.show()
    plt.close()


def rank_parole_plot():
    # Leggi i dati dal file di testo
    with open('output/grafici/rank_parole.txt', 'r') as file:
        lines = file.readlines()

    # Inizializza le liste per l'importanza media delle parole chiave
    real_guide_importance = []
    generated_guide_importance = []

    # Itera sulle righe del file
    for line in lines:
        line = line.strip()
        if line.startswith('!Importance of keywords in the real user guide:'):
            real_guide_importance = []
        elif line.startswith('!Importance of keywords in the generated user guide:'):
            generated_guide_importance = []
        elif line.startswith('!user guide'):
            # Calcola l'importanza media delle parole chiave per la guida reale
            real_mean = np.mean(real_guide_importance) if real_guide_importance else 0.0
            # Calcola l'importanza media delle parole chiave per la guida generata
            generated_mean = np.mean(generated_guide_importance) if generated_guide_importance else 0.0

            # Aggiungi le importanze medie alla lista
            real_guide_importance.append(real_mean)
            generated_guide_importance.append(generated_mean)

        else:
            # Estrai l'importanza dalla riga corrente
            importance = float(line.split(':')[1].strip())
            if generated_guide_importance:
                generated_guide_importance.append(importance)
            else:
                real_guide_importance.append(importance)

    # Calcola la media e la deviazione standard dell'importanza media delle parole chiave
    real_mean = np.mean(real_guide_importance)
    real_std = np.std(real_guide_importance)

    generated_mean = np.mean(generated_guide_importance)
    generated_std = np.std(generated_guide_importance)

    # Controlla se le liste sono vuote e assegna 0 se necessario
    real_mean = real_mean if np.isfinite(real_mean) else 0.0
    real_std = real_std if np.isfinite(real_std) else 0.0
    generated_mean = generated_mean if np.isfinite(generated_mean) else 0.0
    generated_std = generated_std if np.isfinite(generated_std) else 0.0

    # Crea l'istogramma
    index = np.arange(2)
    bar_width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(index, [real_mean, generated_mean], bar_width,
                    yerr=[real_std, generated_std],
                    capsize=10)

    # Etichette sugli assi e titolo del grafico
    ax.set_xlabel('Tipo di User Guide')
    ax.set_ylabel('Importanza Media')
    ax.set_title('Qualità delle User Guide Generate')
    ax.set_xticks(index)
    ax.set_xticklabels(['Reale', 'Generata'])

    # Mostra il grafico
    plt.tight_layout()
    plt.show()

def self_assesment():
    # Lettura dei voti dal file di testo
    with open("output/score_user_guide.txt", 'r') as file:
        lines = file.readlines()
    votes = [int(line.strip()) for line in lines]

    # Creazione dell'istogramma
    plt.hist(votes, bins=10, edgecolor='black', color="green")
    plt.xlabel('Scores')
    plt.ylabel('Frequenza')
    plt.title('Self assesment scores', fontweight="bold")
    plt.savefig("output/grafici/self_assesment_plot.png")
    plt.close()



# main
cosine_similarity_plot()
cosine_similarity_complexity_plot("simple")
cosine_similarity_complexity_plot("moderate")
cosine_similarity_complexity_plot("complex")
word_count_plot()
# genero il grafo con le medie dei nostri voti
file1 = "output/grafici/MEDIA_voti_guide_reali.csv"
file2 = "output/grafici/MEDIA_voti_generated.csv"
create_histogram(file1, file2)
create_histogram_simple(file1, file2)
create_histogram_medium(file1, file2)
create_histogram_complex(file1, file2)
self_assesment()
rank_parole_plot()
