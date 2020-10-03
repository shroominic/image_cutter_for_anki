import numpy as np

class Turtle:

    def __init__(self, image, position = (0, 0)):
        self.position = position
        self.image = image

    def is_pixel_white(self, position = None):
        if position != None:
            pixel = self.image.getpixel(position)
        else: 
            pixel = self.image.getpixel(self.position)
        if pixel < 150:
            return False
        return True

    def move(self, to_move):
        self.position = tuple(np.add(self.position, to_move))

    def move_until_stop(self, direction):
        while(self.is_pixel_white()):
            self.move(direction)

    def get_to_start(self):
        self.position = (0, float(round(self.image.size[1]/2)))

        self.move_until_stop((1, 0))
        
        while(not self.is_pixel_white(tuple(np.add(self.position, (1, 0))))):
            self.move((0, -1))

        self.move((5, 5))

        return self.position

    def move_to_next_card(self):
        self.move_until_stop((0, 1))
        self.move((0, 5))
        return self.position

    def get_card_posisitons(self):
        output = [[(0, 0), (0, 0)],    #Front Positions (start xy, end xy)
                  [(0, 0), (0, 0)]]    #Back  Positions (start xy, end xy)

        output[0][0] = self.position

        self.move_until_stop((1, 0))
        self.move((-2, 0))
        self.move_until_stop((0, 1))
        self.move((0, -2))

        output[0][1] = self.position

        self.move_until_stop((0, -1))
        self.move((5, 2))

        output[1][0] = self.position

        self.move_until_stop((1, 0))
        self.move((-2, 0))
        self.move_until_stop((0, 1))
        self.move((0, -2))

        output[1][1] = self.position

        self.position = output[0][0]
        return output


        