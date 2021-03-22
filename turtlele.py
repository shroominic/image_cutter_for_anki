import numpy as np


class Turtle:

    def __init__(self, image, position=(0, 0)):
        self.position = position
        self.image = image

    def is_pixel_white(self, position=None):
        if position is not None:
            pixel = self.image.getpixel(position)[0]
            return not pixel < 242
        elif not self.out_of_range():
            pixel = self.image.getpixel(self.position)[0]
            return not pixel < 242
        else:
            return True

    def out_of_range(self):
        return not ((self.position[0] >= 0) and
                    (self.position[0] < self.image.width - 1) and
                    (self.position[1] >= 0) and
                    (self.position[1] < self.image.height - 1))

    # changes self.position
    def move(self, to_move):
        self.position = tuple(np.add(self.position, to_move))

    # move until a black pixel
    def move_until_black(self, direction):
        while (not self.out_of_range()) and self.is_pixel_white():
            self.move(direction)

    # move until a white pixel
    def move_until_white(self, direction):
        while (not self.out_of_range()) and (not self.is_pixel_white()):
            self.move(direction)

    # moves to the first row
    def get_to_start(self):
        self.position = (0, float(round(self.image.size[1] / 2)))

        self.move_until_black((1, 0))

        while not self.is_pixel_white(tuple(np.add(self.position, (1, 0)))):
            self.move((0, -1))

        self.move((5, 5))

        return self.position

    # moves to the next row
    def move_to_next_card(self):
        self.move_until_black((0, 1))
        self.move((0, 10))
        return self.position

    # returns a list with positions to crop the cards
    def get_card_positions(self):
        output = [[(0, 0), (0, 0)],
                  [(0, 0), (0, 0)]]

        output[0][0] = self.position  # front start position

        self.move_until_black((1, 0))
        self.move((-2, 0))
        self.move_until_black((0, 1))
        self.move((0, -2))

        output[0][1] = self.position  # front end position

        self.move_until_black((0, -1))
        self.move((5, 2))

        output[1][0] = self.position  # Back start position

        self.move_until_black((1, 0))
        self.move((-2, 0))
        self.move_until_black((0, 1))
        self.move((0, -2))

        output[1][1] = self.position  # Back End Position

        self.position = output[0][0]  # Reset Position
        return output

    # returns True if there is a next card
    def next_card_is_available(self):
        init_position = self.position

        self.move_to_next_card()
        self.move_until_black((1, 0))
        if self.position[0] > (self.image.width - 30):
            return False

        self.position = init_position
        return True
