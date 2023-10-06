import os
from pathlib import Path
from PIL import Image, ImageFilter, ImageOps

dir = Path(r"./image/")
#logo = "./image/logo.png"
#dir_file = "./image/"

def image_load():
    for file in dir.glob("*.jpg"):
        img = Image.open(file)
        cropped_img = img.crop((0,0,2500,4000))
        cropped_img.load()
        cropped_img.show()

image_load()

'''
def image_crop():
    cropped_img = image_load().crop((0,0,2500,4000))
    cropped_img.show()

image_crop()
'''


