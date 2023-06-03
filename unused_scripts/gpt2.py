import gpt_2_simple as gpt2
from nltk.tokenize import sent_tokenize

# Scarica il modello GPT-2 se non è già presente nella directory 'models'
#gpt2.download_gpt2(model_name='124M')

# Carica il modello GPT-2
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, model_name='124M')

# Funzione per generare il riassunto del testo
def genera_riassunto(testo, lunghezza_riassunto):
    # Suddivide il testo in frasi
    frasi = sent_tokenize(testo)
    testo_completo = ' '.join(frasi)

    # Genera il riassunto utilizzando il modello GPT-2
    riassunto = gpt2.generate(sess, run_name='124M', length=lunghezza_riassunto, prefix=testo_completo, return_as_list=True)[0]

    return riassunto

# Test del codice
testo = "Il lavoro svolto presso l'azienda XYZ mi ha permesso di acquisire solide competenze in ambito informatico, grazie alla partecipazione a progetti innovativi e di grande valore. Ho sviluppato competenze tecniche in diversi linguaggi di programmazione,   come Java, Python e C++, e ho imparato a lavorare con database relazionali e non relazionali. Inoltre, ho acquisito abilità nella gestione di progetti, coordinando     le attività di una piccola squadra di sviluppatori. Sono sempre stato orientato al raggiungimento degli obiettivi aziendali e alla soddisfazione del cliente"
lunghezza_riassunto = 50

riassunto = genera_riassunto(testo, lunghezza_riassunto)
print("Riassunto:")
print(riassunto)
