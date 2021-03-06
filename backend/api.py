try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import re
import os

# tesseract_cmd  = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
tesseract_cmd  = r'/usr/bin/tesseract'
def read_label(tesseract_cmd, image_path):
    img = Image.open(os.path.abspath(image_path))
    #img = cv2.imread(image_path) # Won't work on Ubuntu? or Tesseract 3.04?
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    label_text = pytesseract.image_to_string(img)


    nutrition_map = {}
    #print(label_text)
    startparse = False
    for line in label_text.splitlines():
        if startparse:
            line += " "
            m = re.findall('([^0-9.]* / [^0-9.]*) (\d+.?\d*\s*(?:mg|g)? (?!%))?\s*(\d+\s*%)?', line)
            #for ff in m:
                #print(m)
            if len(m) > 0:
                name = re.search('([^0-9.]*) / [^0-9.]*', m[0][0])
                nutrition_map[name.group(1)] = {}
                nutrition_map[name.group(1)]["amount"] = m[0][1]
                nutrition_map[name.group(1)]["daily_percent"] = m[0][2]

        if line == "Teneur % valeur quotidienne":
            startparse = True

    return nutrition_map


def parse_ingredients(tesseract_cmd, image_path):
    img = cv2.imread(image_path)
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    label_text = pytesseract.image_to_string(img)

    nutrition_map = {}
    print(label_text)
    startparse = False
    m = re.findall('INGREDIENTS:((.+\s)*)', label_text)
    ingredients =m[0][0].replace('\n', ' ')
    ingredients = ingredients.split(',')
    return ingredients
