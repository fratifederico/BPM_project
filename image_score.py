from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Carica le immagini originali
ssim_scores_dalle = []
ssim_scores_mid = []

for i in range(21):
    image_dalle = Image.open("images/dalle_images/" + str(i) + ".png")
    image_mid = Image.open("images/midjourney_images/" + str(i) + ".png")
    image_real = Image.open("images/real_images/" + str(i) + ".png")

    # Ottieni le dimensioni dell'immagine real
    real_width, real_height = image_real.size

    # Ridimensiona le immagini
    image_dalle = image_dalle.resize((real_width, real_height))
    image_mid = image_mid.resize((real_width, real_height))

    # Converti le immagini in array NumPy in scala di grigi
    array_real = np.array(image_real.convert("L"))
    array_dalle = np.array(image_dalle.convert("L"))
    array_mid = np.array(image_mid.convert("L"))

    # Calcola gli score SSIM
    score_dalle = ssim(array_real, array_dalle)
    score_mid = ssim(array_real, array_mid)

    # Memorizza gli score SSIM nelle rispettive liste
    ssim_scores_dalle.append(score_dalle)
    ssim_scores_mid.append(score_mid)

# Calcola le medie dei punteggi SSIM
mean_ssim_dalle = np.mean(ssim_scores_dalle)
mean_ssim_mid = np.mean(ssim_scores_mid)

# Crea un array di indici per l'asse x
indices = np.arange(21)

# Crea il plot a istogramma
plt.bar(indices, ssim_scores_dalle, width=0.35, label='DALL-E')
plt.bar(indices + 0.35, ssim_scores_mid, width=0.35, label='Midjourney')

# Aggiungi le medie al plot come linee
plt.axhline(mean_ssim_mid, color='g', linestyle='--', label='Media Midjourney')
plt.axhline(mean_ssim_dalle, color='b', linestyle='--', label='Media DALL-E')


# Aggiungi le etichette agli assi
plt.xlabel('Numero Immagine')
plt.ylabel('Score SSIM')
plt.title('Confronto SSIM tra DALL-E e Midjourney', fontweight="bold")
plt.xticks(indices + 0.35 / 2, range(21))
plt.legend()

# Mostra il plot
plt.savefig("output/grafici/SSIM.png")
plt.close()
