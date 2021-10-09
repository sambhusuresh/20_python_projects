 import pytesseract
 import osfrom PIL import image

 pytesseract.pytesseract.tesseract_cmd =  #"file path"

 def convert():
     img =  image.open('imag.jpg')
     text = pytesseract.image_to_text
     print(text)