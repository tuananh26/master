import arcade

from image import path_img_x, path_img_o
from calculate import calculate_center_position_from_index
from const import IMAGE_SCALING


class Chess:
    def __init__(self, type, width_index, height_index):
        if(type == True):
            self.img = arcade.Sprite(path_img_x, IMAGE_SCALING)
        else:
            self.img = arcade.Sprite(path_img_o, IMAGE_SCALING)

        self.img.center_x = calculate_center_position_from_index(width_index)
        self.img.center_y = calculate_center_position_from_index(height_index)
