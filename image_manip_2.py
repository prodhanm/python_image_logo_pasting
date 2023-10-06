import os
from PIL import Image, ImageFilter, ImageOps

filename = "./image/image1.jpg"
logo = "./image/logo.png"
dir_file = "./image/"

def image_load():
    with Image.open(filename) as img, \
        Image.open(logo) as logo_img:
        img.load()
        img.show()

image_load()