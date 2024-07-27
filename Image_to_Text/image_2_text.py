from PIL import Image
import pytesseract
import cv2


# https://github.com/UB-Mannheim/tesseract
img_path = r"image/Test2.png"
pytesseract.pytesseract.tesseract_cmd = r'Tesseract\tesseract.exe'

def image_ocr(image_path):
    text = pytesseract.image_to_string(image_path,lang='vie')
    # text = pytesseract.image_to_string(image_path, lang='eng+ces', config='--psm 1')
    print(text)

image_ocr(img_path)
