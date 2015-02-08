import copy
import math


class SquareOrderedAlgorithm(object):

    def process(self, sprite):
        num_images = len(sprite.images)
        max_width = round(math.sqrt(num_images))
        x = 0
        y = 0
        for image in sprite.images:
            if (x >= max_width):
                x = 0
                y += 1
            image.x = x * image.absolute_width
            image.y = y * image.absolute_height
            x += 1
