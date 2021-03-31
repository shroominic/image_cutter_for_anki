from PIL import Image
import os
import turtle
import anki


image_path_list = os.listdir('math_images')
image_list = []

for path in image_path_list:
    if path.endswith('.jpg'):
        image_list.append(Image.open(f'math_images/{path}'))


def create_card(input_image, positions, counter):
    card_front = input_image.crop((
        positions[0][0][0],
        positions[0][0][1],
        positions[0][1][0],
        positions[0][1][1]))
    card_back = input_image.crop((
        positions[1][0][0],
        positions[1][0][1],
        positions[1][1][0],
        positions[1][1][1]))
    card_front.save(f'./result/card_{counter}_front.jpg')
    card_back.save(f'./result/card_{counter}_back.jpg')


card_counter = 0

for image in image_list:
    print(image)
    turtle = turtle.Turtle(image)

    turtle.get_to_start()
    while True:
        try:
            turtle.move_to_next_card()
            create_card(image, turtle.get_card_positions(), card_counter)
            anki.my_deck.add_note(
                anki.create_card_from_images(
                    f'card_{card_counter}_front.jpg',
                    f'card_{card_counter}_back.jpg'
                ))
            card_counter += 1

        except:
            break

anki.create_apkg_file()
