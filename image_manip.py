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
    # The size, format and mode, displays data that can 
    # be utilized for image manipulation.
    #img.show()

    cropped_img = img.crop((0,0,2500,4000))
    cropped_img.show()
    crop_size = cropped_img.size
    print(f"crop_img1 = {crop_size}")
    # img.crop = (x,y, w+x, h+y)
    # x,y can be the coordinates to start and w+x or y+h
    # is a way to add the reduced size to the coordinates.
    # This way the image is cropped below the actual size.