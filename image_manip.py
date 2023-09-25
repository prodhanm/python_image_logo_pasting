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
    #cropped_img.show()
    crop_size = cropped_img.size
    print(f"crop_img1 = {crop_size}")
    # img.crop = (x,y, w+x, h+y)
    # x,y can be the coordinates to start and w+x or y+h
    # is a way to add the reduced size to the coordinates.
    # This way the image is cropped below the actual size.

    img_rotate = cropped_img.rotate(
        -90, expand=True, center=(500,500)
        )
    #img_rotate.show()
    # the rotate() takes a geometrical angle as an argument,
    # and the value can be positive or negative, depending 
    # on the orientation of the image. The image has been 
    # #cropped to center the image of the
    # child at the tuple: (500,600). 

    img_resize = img_rotate.resize(
        (700,500)
    )
    img_resize.size
    #img_resize.show()
    print(f"resized = {img_resize}")
    # When the image is resized after some aspects of image
    # maipulation, it is able to be resized to the size that
    # is desired, to still maintain the clarity of the image.

    img_convert = img_resize.convert("L")
    img_convert.show()

    #with open(logo) as logo:
