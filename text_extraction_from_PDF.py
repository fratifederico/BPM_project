import fitz


def extract_text_from_pdf(file_path):
    """
       Estrae il testo da un file PDF.

       Args:
           file_path (str): Il percorso del file PDF da cui estrarre il testo.

       Returns:
           str: Il testo estratto dal file PDF.

       """
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        page_text = page.get_text()
        if "Powered by TCPDF" in page_text:
            page_text = page_text.replace("Powered by TCPDF (www.tcpdf.org)", "")
        text += page_text

    doc.close()

    return text

