import arcade

from image import path_img_x, path_img_o
from calculate import calculate_center_position_from_index
from const import IMAGE_SCALING


class Chess:
    def __init__(self, type, index_x, index_y):
        self.type = type
        self.index_x = index_x
        self.index_y = index_y
        if(type == True):
            self.img = arcade.Sprite(path_img_x, IMAGE_SCALING)
        else:
            self.img = arcade.Sprite(path_img_o, IMAGE_SCALING)

        self.img.center_x = calculate_center_position_from_index(index_x)
        self.img.center_y = calculate_center_position_from_index(index_y)
