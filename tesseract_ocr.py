import cv2  
import pytesseract
from PIL import Image
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# image = cv2.imread("sample.png")

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# #gray = cv2.threshold(gray , 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]

# cv2.imwrite("processed.png",gray)

text = pytesseract.image_to_string(Image.open("processed.png"))
print(text)