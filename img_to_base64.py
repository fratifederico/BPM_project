import base64


def img_to_base64(img_path):
    """
        Converte un'immagine in formato JPEG in una stringa di dati base64.

        Args:
            img_path (str): Il percorso dell'immagine da convertire.

        Returns:
            str: La stringa di dati base64 che rappresenta l'immagine convertita.

        """
    with open(img_path, "rb") as image_file:
        image_data = image_file.read()
        image = "data:image/jpeg;base64," + base64.b64encode(image_data).decode("utf-8")
    return image
