import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

# Funzione per calcolare la frequenza delle parole
def calcola_frequenza_parole(testo):
    parole = word_tokenize(testo)
    parole_importanti = [parola for parola in parole if parola.lower() not in stopwords.words('italian')]
    frequenza = FreqDist(parole_importanti)
    return frequenza

# Funzione per generare il riassunto del testo
def genera_riassunto(testo, lunghezza_riassunto):
    frasi = sent_tokenize(testo)
    frequenza_parole = calcola_frequenza_parole(testo)
    valutazione_frasi = [(frase, sum([frequenza_parole[parola] for parola in word_tokenize(frase.lower()) if parola.isalpha()]))
                        for frase in frasi]

    valutazione_frasi_ordinate = sorted(valutazione_frasi, key=lambda x: x[1], reverse=True)
    frasi_riassunto = [valutazione[0] for valutazione in valutazione_frasi_ordinate[:lunghezza_riassunto]]

    riassunto = ' '.join(frasi_riassunto)
    return riassunto

# Test del codice
testo = "Il lavoro svolto presso l'azienda XYZ mi ha permesso di acquisire solide competenze in ambito informatico, grazie alla partecipazione a progetti innovativi e di grande valore. Ho sviluppato competenze tecniche in diversi linguaggi di programmazione,   come Java, Python e C++, e ho imparato a lavorare con database relazionali e non relazionali. Inoltre, ho acquisito abilità nella gestione di progetti, coordinando     le attività di una piccola squadra di sviluppatori. Sono sempre stato orientato al raggiungimento degli obiettivi aziendali e alla soddisfazione del cliente"
riassunto = genera_riassunto(testo, 2)
print("Riassunto:")
print(riassunto)