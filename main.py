import os
from PIL import Image

os.chdir('images')

image_path_list = os.listdir()
image_list = []

for path in image_path_list:
    image_list.append(Image.open(path))

turtle = (1, 1)

def is_pixel_white(pixel):
    if pixel != 255:
        return False
    return True

def turtle_movement(image):
    turtle = (0, image.size[1]/2)
    pixel = image.getpixel(turtle)

    while(is_pixel_white(pixel)):
        turtle = (turtle[0] + 1, turtle[1])
        pixel = image.getpixel(turtle)

    return turtle


print(turtle_movement(image_list[1]))

for image in image_list: #Going through Images in image_list
    pass
