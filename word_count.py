import re

def word_count(input_string):
    """
        Questa funzione conta il numero di parole in una stringa di input. Cerca anche di pulire la stringa rimuovendo
        eventuali "parole" da non considerare,ad esempio ": , ; ! ? = & % ..."

        Args:
            input_string (str): La stringa di input da elaborare.

        Returns:
            int: Il numero di parole nella stringa di input.
        """
    cleaned_string = re.sub(r'[;,:!?$%&?=]', '', input_string)
    words = cleaned_string.split()
    return len(words)
