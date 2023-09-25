from PIL import Image

filename = "./image/image1.jpg"
logo = "./image/logo.png"

with Image.open(filename) as img:
    img.load()
    size = img.size
    print(f"size = {size}")
    format = img.format
    print(f"format = {format}")
    mode = img.mode
    print(f"mode = {mode}")
    #img.show()
