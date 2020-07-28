import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
content = pytesseract.image_to_string('one_extract.png')
print(content)