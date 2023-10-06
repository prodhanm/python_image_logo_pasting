import os
from pathlib import Path
from PIL import Image, ImageFilter, ImageOps

dir = Path(r"./image/")
#logo = "./image/logo.png"
#dir_file = "./image/"

def file_rename():
    p = Path(dir/"image4.JPG")
    #if "*.JPG" in dir:
    img_rename = Path("image4.jpg")
    f = p.rename(img_rename)
    return f

def image_load(dir):
    logo = Image.open(dir/"logo.png")
    print(logo.size)
    logo.load()
    for file in dir.glob("*.jpg"):
        img = Image.open(file)
        img.load()
        cropped_img = img.crop((0,0,2500,4000))
        #image_convert = cropped_img.convert("L")
        logo_conv = logo.convert("L")
        #threshold = 50, substituting number on conditional statement
        logo_func = logo_conv.point(lambda x:255 if x > 50 else 0)
        #logo_resize = logo_func.resize((300,81))
        logo_filter = logo_func.filter(ImageFilter.CONTOUR)
        logo_trans = logo_filter.point(lambda x: 0 if x ==255 else 255)
        cropped_img.paste(logo_trans, (0,0), logo_trans)
        #image_convert.load()
        #cropped_img.show()

image_load(dir)