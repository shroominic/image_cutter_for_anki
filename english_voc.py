from PIL import Image
import os
import turtlele
import numpy as np

image_path_list = os.listdir('./english_voc_images')
image_path_list.sort()
image_list = []
card_counter = 0

for path in image_path_list:
    if '.jpg' in path:
        image_list.append(Image.open(f'./english_voc_images/{path}'))


def create_card(input_image, positions, counter, text):
    card_english = input_image.crop((
        positions[0][0][0],
        positions[0][0][1],
        positions[0][1][0],
        positions[0][1][1]))
    card_german = input_image.crop((
        positions[1][0][0],
        positions[1][0][1],
        positions[1][1][0],
        positions[1][1][1]))
    card_extra = input_image.crop((
        positions[2][0][0],
        positions[2][0][1],
        positions[2][1][0],
        positions[2][1][1]))
    card_english.save(f'./result/{text}_card_{counter}_english.jpg')
    card_german.save(f'./result/{text}_card_{counter}_german.jpg')
    card_extra.save(f'./result/{text}_card_{counter}_extra.jpg')


class EnglishTurtle(turtlele.Turtle):

    def get_to_start(self):
        self.position = (float(round(self.image.size[0] / 1.35)), 0.)

        self.move_until_black((0, 1))
        self.move((0, 5))
        self.move_until_black((0, 1))

        while not self.is_pixel_white(tuple(np.add(self.position, (0, 1)))):
            self.move((-1, 0))

        self.move((10, 15))
        if not self.is_pixel_white():
            self.move_until_white((0, 1))
            self.move((0, 5))

    def get_card_positions(self):
        output = [[(0, 0), (0, 0)],
                  [(0, 0), (0, 0)],
                  [(0, 0), (0, 0)]]

        init_position = self.position

        self.move_until_black((1, 0))
        self.move((10, 0))

        output[0][0] = self.position  # front start position

        self.move_until_black((1, 0))
        self.move((-8, 0))
        self.move_until_black((0, 1))
        self.move((0, -8))

        output[0][1] = self.position  # front end position

        self.move_until_black((0, -1))
        self.move((15, 8))

        output[1][0] = self.position  # Back start position

        self.move_until_black((1, 0))
        self.move((-5, 0))
        self.move_until_black((0, 1))
        self.move((0, -5))

        output[1][1] = self.position  # Back End Position

        self.move_until_black((0, -1))
        self.move((10, 5))

        output[2][0] = self.position  # Extra Start Position

        self.move_until_black((0, 1))
        while not self.is_pixel_white(tuple(np.add(self.position, (0, 1)))):
            self.move((1, 0))
        self.move((-5, -5))

        output[2][1] = self.position  # Extra End Position

        self.position = init_position  # Reset Position
        return output


for image in image_list:
    turtle = EnglishTurtle(image)
    turtle.get_to_start()

    debug_start_position = turtle.position

    #print(f'Image: {image.filename} \nStart Position: {turtle.position}')
    while turtle.next_card_is_available():
        if not turtle.is_pixel_white():
            turtle.move_until_white((0, 1))
            turtle.move((0, 5))
        try:
            card_position = turtle.get_card_positions()
            create_card(image, card_position, card_counter, image.filename[21:-4])
            card_counter += 1
            turtle.move_to_next_card()
        except:
            print(f'Error: {image.filename} - {turtle.position} - Start: {debug_start_position}')
            os.rename(image.filename, f'error/{image.filename}')
            break
