# USAGE
# python normal_OCR.py -i image1.jpg

# import necessary packages
import cv2
import pytesseract
import numpy as np
import argparse

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the Input Image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])

# convert to text
txt = pytesseract.image_to_string(image)

# display
print(txt)


