import os
from pathlib import Path
from PIL import Image, ImageFilter, ImageOps

dir = Path(r"./image/")
#logo = "./image/logo.png"
#dir_file = "./image/"

def image_load():
    for file in dir.glob("*.jpg"):
        img = Image.open(file)
        img.load()
        img.show()
            
image_load()

