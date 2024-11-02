import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import cv2
import os

# Establece la ruta a Tesseract OCR en caso de que sea necesario (en Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def pdf_to_text(pdf_path):
    # Convierte cada página del PDF en una imagen
    pages = convert_from_path(pdf_path, dpi=300)
    text = ""

    for page_number, page in enumerate(pages):
        # Convierte la página en un archivo de imagen temporal
        page.save(f"page_{page_number}.jpg", "JPEG")
        
        # Lee la imagen con OpenCV para mejorarla si es necesario
        image = cv2.imread(f"page_{page_number}.jpg")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        
        # Usa OCR en la imagen procesada
        page_text = pytesseract.image_to_string(thresh, lang='spa')  # Cambia 'spa' por el idioma necesario
        text += page_text + "\n\n"

        # Borra la imagen temporal
        os.remove(f"page_{page_number}.jpg")

        if page_numer == 2:
            break

    return text

# Usa la función para convertir un PDF escaneado en texto
pdf_path = "1866-becerro-de-las-behetricc81as.pdf"
texto_extraido = pdf_to_text(pdf_path)
print(texto_extraido)