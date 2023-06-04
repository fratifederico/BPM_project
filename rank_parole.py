from nltk.probability import FreqDist
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from text_extraction_from_PDF import extract_text_from_pdf


# Aggiungi la seguente linea per verificare se i dati sono già presenti
if not nltk.data.find('tokenizers/punkt'):
    nltk.download('punkt')

if not nltk.data.find('corpora/stopwords'):
    nltk.download('stopwords')


def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    tagged_tokens = pos_tag(tokens)  # Applichiamo il POS tagging ai token
    lemmatizer = WordNetLemmatizer()
    filtered_tokens = []
    for token, tag in tagged_tokens:
        if len(token) > 1 and token.isalpha() and token not in stop_words and (
                tag.startswith('N') or tag.startswith('V')):
            if tag.startswith('N'):
                lemma = lemmatizer.lemmatize(token, pos='n')  # Lemmatizzazione per sostantivi
            elif tag.startswith('V'):
                lemma = lemmatizer.lemmatize(token, pos='v')  # Lemmatizzazione per verbi
            else:
                lemma = token
            filtered_tokens.append(lemma)
    return filtered_tokens


def get_top_keywords(text, num_keywords):
    tokens = preprocess_text(text)
    freq_dist = FreqDist(tokens)
    total_words = len(tokens)
    top_keywords = freq_dist.most_common(num_keywords)
    normalized_keywords = [(word, count / total_words) for word, count in top_keywords]
    return normalized_keywords


def plot_histogram(keywords1, keywords2, i):
    words1, counts1 = zip(*keywords1)
    words2, counts2 = zip(*keywords2)

    all_words = set(words1).union(set(words2))
    index = np.arange(len(all_words))
    bar_width = 0.35

    counts1_dict = dict(keywords1)
    counts2_dict = dict(keywords2)

    counts1_combined = [counts1_dict.get(word, 0) for word in all_words]
    counts2_combined = [counts2_dict.get(word, 0) for word in all_words]

    fig, ax = plt.subplots()

    if i in [1, 3, 5, 11, 13, 14]:  # complex
        colors = ["#ffd700", "#006400"]
    elif i in [6, 7, 8, 10, 15, 17, 18, 19]:  # moderate
        colors = ["#008000", "#ff0000"]
    elif i in [0, 2, 4, 9, 12, 16, 20]:  # simple
        colors = ['#00ffff', '#000080']

    ax.bar(index, counts1_combined, bar_width, label='Real User Guide', color=colors[0])
    ax.bar(index + bar_width, counts2_combined, bar_width, label='Generated User Guide', color=colors[1])

    ax.set_xlabel('Keywords')
    ax.set_ylabel('Frequency')
    ax.set_title('Keywords Comparison for User Guide nr.:' + str(i))
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(all_words, rotation=90)
    ax.legend()

    plt.tight_layout()
    plt.savefig("output/grafici/plot_ranks/grafico_rank_parole" + str(i) + ".png")

    # printo su terminale
    # Stampa delle importanze delle parole in terminale
    with open("output/grafici/rank_parole.txt", "a") as file:
        file.write("!user guide:" + str(i) + "\n")
        file.write("!Importance of keywords in the real user guide:\n")
        for word, count in keywords1:
            word = word.replace('\ufb00', 'ff')
            word = word.replace('\u02ce', '')
            word = word.replace('\u02cb', '')
            file.write(f"{word}: {count}" + "\n")
        file.write("!Importance of keywords in the generated user guide:\n")
        for word, count in keywords2:
            word = word.replace('\ufb00', 'ff')
            word = word.replace('\u02ce', '')
            word = word.replace('\u02cb', '')
            file.write(f"{word}: {count}" + "\n")

    # plt.show()


def plot_rank_parole(text1, text2, num_keywords, index):
    """
    La funzione costruisce un grafo sull'importanza delle parole delle user guide
        args:
            (str) text1,text2: text string relatives to the 2 text to analyze
            num_keywords: the number of the top keywords to include into the plot
            index: an integer representing how to save the plot (e.g: plot0.png, plot1.png,...)
        returns:
            nothing, just shows the plot
    """
    top_keywords1 = get_top_keywords(text1, num_keywords)
    top_keywords2 = get_top_keywords(text2, num_keywords)
    plot_histogram(top_keywords1, top_keywords2, index)


i = 0
for i in range(21):
    real_user_guide = extract_text_from_pdf("real_user_guides_pdf/" + str(i) + ".pdf")
    generated_user_guide = extract_text_from_pdf("output/user_guides_generated/" + str(i) + ".pdf")
    plot_rank_parole(real_user_guide, generated_user_guide, 15, i)
