from PIL import Image
import os

dir_name = "./image/"

def img_rename(dir_name):
    for index, dir in enumerate(os.listdir(dir_name), 1):
        with Image.open(dir) as filename:
            if dir.endswith(".jpg"):
                fn, fext = os.path.splitext(dir)
                fn.replace("image", "mufassa")
                dir.os.join(fn,index,fext)
                print(dir)

img_rename(dir_name)