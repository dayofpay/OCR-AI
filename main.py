import cv2
import pytesseract
import sys
import array
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class Config:
    def __init__(
        self, minimumWordLength, maxWordLength=sys.maxsize, problemDetectionText=None
    ):
        self.minimumWordLength = minimumWordLength
        self.maxWordLength = maxWordLength
        self.problemDetectionText = problemDetectionText

    def getMinimumWordLength(self):
        return self.minimumWordLength

    def getMaximumWordLength(self):
        return self.maxWordLength


language = input(
    "Enter the language code of the language pack you want to use (e.g. eng for English, bul for Bulgarian): "
)
imageName = input("Please insert the image here: ")

softwareConfig = Config(1, sys.maxsize, "[!] Problem Detected : ")

minimum_word_length = softwareConfig.getMinimumWordLength()

config = r"--psm 11"

lang = language.lower()

img = cv2.imread(imageName)


text = pytesseract.image_to_string(img, config=config, lang=lang)


lines = text.split("\n")


non_empty_lines = [line.strip() for line in lines if line.strip()]


invalidWords = []


validWords = []

for word in non_empty_lines:
    if len(word) <= softwareConfig.getMinimumWordLength():
        invalidWords.append(word)
    elif len(word) >= softwareConfig.getMaximumWordLength():
        invalidWords.append(word)
    else:
        validWords.append(word)


print("Printing all invalid words ...")


print("------------------")
time.sleep(2)


for invalidWord in invalidWords:
    print(softwareConfig.problemDetectionText + word)

print("Printing all valid words ...")


print("------------------")


time.sleep(2)


for validWord in validWords:
    print(validWord)
