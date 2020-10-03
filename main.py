from PIL import Image
import os
import turtlele

os.chdir('images')

image_path_list = os.listdir()
image_list = []

for path in image_path_list:
    if path.endswith('.jpg'):
        image_list.append(Image.open(path))

def create_card(image, positions, counter):
    card_front = image.crop((
        positions[0][0][0], 
        positions[0][0][1], 
        positions[0][1][0], 
        positions[0][1][1]))
    card_back = image.crop((
        positions[1][0][0], 
        positions[1][0][1], 
        positions[1][1][0], 
        positions[1][1][1]))
    card_front.save(f'card_{counter}_front.jpg')
    card_back.save(f'card_{counter}_back.jpg')

os.chdir('./result')

card_counter = 0

for image in image_list:
    print(image)
    turtle = turtlele.Turtle(image)
    
    turtle.get_to_start()
    while True:
        try:
            turtle.move_to_next_card()
            create_card(image, turtle.get_card_posisitons(), card_counter)
            card_counter += 1

        except:
            break
    
    
    