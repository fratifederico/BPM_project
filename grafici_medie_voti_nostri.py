import matplotlib.pyplot as plt
import pandas as pd


def create_histogram(file1, file2):
    # Leggi i dati dai file CSV
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Calcola la media delle colonne
    means1 = df1.mean()
    means2 = df2.mean()

    # Seleziona solo le colonne di interesse (escludendo l'indice)
    columns = df1.columns[1:]

    # Crea un DataFrame con le medie delle colonne
    data = pd.DataFrame({'Guide Reali': means1[1:], 'Guide Generate': means2[1:]}, index=columns)

    # Crea il grafico a barre
    fig, ax = plt.subplots(figsize=(12, 6))
    data.plot(kind='bar', ax=ax)
    ax.set_xlabel('Categorie')
    ax.set_ylabel('Media')
    ax.set_title('Confronto tra guide reali e guide generate', fontweight='bold')
    ax.set_xticklabels(data.index, rotation=0)
    ax.tick_params(axis='x', labelsize=7)  # Riduzione del font sull'asse x
    ax.tick_params(axis='y', labelsize=10)  # Riduzione del font sull'asse y
    plt.savefig("output/grafici/our_scores_plot.png", bbox_inches='tight')
    plt.close()


def create_histogram_simple(file1, file2):
    # Leggi i dati dai file CSV
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    df1 = df1.iloc[[0, 2, 4, 9, 12, 16, 20]]
    df2 = df2.iloc[[0, 2, 4, 9, 12, 16, 20]]

    colors = ['#00ffff', '#000080']

    # Calcola la media delle colonne
    means1 = df1.mean()
    means2 = df2.mean()

    # Seleziona solo le colonne di interesse (escludendo l'indice)
    columns = df1.columns[1:]

    # Crea un DataFrame con le medie delle colonne
    data = pd.DataFrame({'Guide Reali Oggetti Semplici': means1[1:], 'Guide Generate Oggetti Semplici': means2[1:]}, index=columns)

    # Crea il grafico a barre
    fig, ax = plt.subplots(figsize=(12, 6))
    data.plot(kind='bar', ax=ax, color=colors)
    ax.set_xlabel('Categorie')
    ax.set_ylabel('Media')
    ax.set_title('Comparison between real and generated user guides for Simple Products', fontweight='bold')
    ax.set_xticklabels(data.index, rotation=0)
    ax.tick_params(axis='x', labelsize=7)  # Riduzione del font sull'asse x
    ax.tick_params(axis='y', labelsize=10)  # Riduzione del font sull'asse y
    plt.savefig("output/grafici/our_scores_simple_product_plot.png", bbox_inches='tight')
    plt.close()


def create_histogram_medium(file1, file2):
    # Leggi i dati dai file CSV
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    df1 = df1.iloc[[6, 7, 8, 10, 15, 17, 18, 19]]
    df2 = df2.iloc[[6, 7, 8, 10, 15, 17, 18, 19]]

    colors = ["#008000", "#ff0000"]

    # Calcola la media delle colonne
    means1 = df1.mean()
    means2 = df2.mean()

    # Seleziona solo le colonne di interesse (escludendo l'indice)
    columns = df1.columns[1:]

    # Crea un DataFrame con le medie delle colonne
    data = pd.DataFrame({'Guide Reali Oggetti Media Complessità': means1[1:], 'Guide Generate Oggetti Media Complessità': means2[1:]}, index=columns)

    # Crea il grafico a barre
    fig, ax = plt.subplots(figsize=(12, 6))
    data.plot(kind='bar', ax=ax, color=colors)
    ax.set_xlabel('Categorie')
    ax.set_ylabel('Media')
    ax.set_title('Comparison between real and generated user guides for Moderate complexity Products', fontweight='bold')
    ax.set_xticklabels(data.index, rotation=0)
    ax.tick_params(axis='x', labelsize=7)  # Riduzione del font sull'asse x
    ax.tick_params(axis='y', labelsize=10)  # Riduzione del font sull'asse y
    plt.savefig("output/grafici/our_scores_medium_product_plot.png", bbox_inches='tight')
    plt.close()


def create_histogram_complex(file1, file2):
    # Leggi i dati dai file CSV
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    df1 = df1.iloc[[1, 3, 5, 11, 13, 14]]
    df2 = df2.iloc[[1, 3, 5, 11, 13, 14]]

    colors = ["#ffd700", "#006400"]

    # Calcola la media delle colonne
    means1 = df1.mean()
    means2 = df2.mean()

    # Seleziona solo le colonne di interesse (escludendo l'indice)
    columns = df1.columns[1:]

    # Crea un DataFrame con le medie delle colonne
    data = pd.DataFrame({'Guide Reali Oggetti Complessi': means1[1:], 'Guide Generate Oggetti Complessi': means2[1:]}, index=columns)

    # Crea il grafico a barre
    fig, ax = plt.subplots(figsize=(12, 6))
    data.plot(kind='bar', ax=ax, color=colors)
    ax.set_xlabel('Categorie')
    ax.set_ylabel('Media')
    ax.set_title('Comparison between real and generated user guides for Complex Products', fontweight='bold')
    ax.set_xticklabels(data.index, rotation=0)
    ax.tick_params(axis='x', labelsize=7)  # Riduzione del font sull'asse x
    ax.tick_params(axis='y', labelsize=10)  # Riduzione del font sull'asse y
    plt.savefig("output/grafici/our_scores_complex_product_plot.png", bbox_inches='tight')
    plt.close()

