import cv2
from numpy import imag  
import pytesseract
from PIL import Image



# Insert your pytesseract location here after installing
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocessing(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #gray = cv2.threshold(gray , 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]

    cv2.imwrite("processed.png",gray)

def read_text():
    text = pytesseract.image_to_string(Image.open("processed.png"))
    print(text)
image = cv2.imread("sample.png")
preprocessing(image)
read_text()