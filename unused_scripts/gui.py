import tkinter as tk

def button_click():
    # Codice da eseguire quando il pulsante viene premuto
    label.config(text="Hai premuto il pulsante!")

# Creazione della finestra principale
window = tk.Tk()

# Creazione di un'etichetta
label = tk.Label(window, text="Ciao, sono un'etichetta!")
label.pack()

# Creazione di un pulsante
button = tk.Button(window, text="Premimi!", command=button_click)
button.pack()

# Avvio del ciclo di eventi della GUI
window.mainloop()