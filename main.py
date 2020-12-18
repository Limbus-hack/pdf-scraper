from PyPDF2 import PdfFileReader
import requests
import io
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os


def OCR(pdf):
    pdfName = pdf.split('.pdf')[0]
    pages = convert_from_path(pdf, 500)
    image_counter = 1
    for page in pages:
        filename = "page_" + str(image_counter) + ".jpg"
        page.save(pdfName + filename, 'JPEG')
        image_counter = image_counter + 1
    filelimit = image_counter - 1
    f = open(pdfName + ".txt", "wb")
    text = ''
    for i in range(1, filelimit + 1):
        filename = pdfName + "page_" + str(i) + ".jpg"
        text += str(((pytesseract.image_to_string(Image.open(filename)))))
        text = text.replace('-\n', '')
        text = text.replace('\n', ' \n')
        os.remove(pdfName + "page_" + str(i) + ".jpg")
    f.write(text.encode('utf-8', 'replace'))
    f.close()
    return text


def main():
    pdf_path = '1.pdf'
    print(OCR(pdf_path))


if __name__ == '__main__':
    main()
