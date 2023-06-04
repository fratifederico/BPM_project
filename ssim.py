import numpy as np
from skimage.metrics import structural_similarity as ssim


def image_score(image1, image2):
    """
    Calcola l'indice SSIM (Structural Similarity Index) tra due immagini.

    Args:
        image1 (PIL.Image.Image): La prima immagine.
        image2 (PIL.Image.Image): La seconda immagine.

    Returns:
        float: L'indice SSIM tra le due immagini, con un valore compreso tra 0 e 1.

    """
    # Determina le dimensioni di destinazione
    target_width = min(image1.width, image2.width)
    target_height = min(image1.height, image2.height)

    # Ridimensiona le immagini
    image1 = image1.resize((target_width, target_height))
    image2 = image2.resize((target_width, target_height))

    # Converti le immagini in array NumPy
    array1 = np.array(image1)
    array2 = np.array(image2)

    # Calcola l'indice SSIM
    ssim_score = ssim(array1, array2, multichannel=True)
    return ssim_score


