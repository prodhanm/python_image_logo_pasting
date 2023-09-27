from PIL import Image, ImageFilter

filename = "./image/image1.jpg"
logo = "./image/logo.png"
with Image.open(filename) as img, \
    Image.open(logo) as logo_img:
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
    #img_convert.show()
    # The image is converted to greyscale, as "L" denotes
    # greyscale. Other indicators can be found on the Pillow
    # 10.0.0 documentation: 
    # https://pillow.readthedocs.io/en/stable/reference/Image.html

    logo_conv = logo_img.convert("L")
    threshold = 50
    logo_func = logo_conv.point(lambda x:255 if x > threshold else 0)
    logo_resize = logo_func.resize(
        (150,50)
    )
    logo_filter = logo_resize.filter(ImageFilter.CONTOUR)
    logo_trans = logo_filter.point(lambda x: 0 if x ==255 else 255)
    img_convert.paste(logo_trans, (150,300), logo_trans)
    print(img_convert.size)
    #img_convert.save("./image/image1_1.jpg")
    '''
    The operation from line 54 to 63, is the process with which
    a secondary image in a .png format is overlaying on a .jpg 
    image. The process allows for the logo image file to be 
    greyscaled via the convert() and then with the use of the 
    point(), we embed a lambda function to create an image of the 
    .png file to paste it onto the .jpg image file. Prior to 
    finalizing the .png file into the image, the .png image file uses
    another lambda function to allow the signature that is to be 
    pasted onto the .jpg image file to go from translucent image to
    a filled image that will allow the image to stand out on the .jpg 
    image. Once pasted, the final result is the picture contains 
    a signature or a logo, as is the result from the commented out use 
    of the save() to get the final product as image1_1.jpg."
    '''
