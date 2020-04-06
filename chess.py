import arcade

from image import path_img_x, path_img_o
from calculate import calculate_center_position_from_index, abs
from const import IMAGE_SCALING, NUMBER_COLUMN, NUMBER_ROW


class Chess:
    def __init__(self, type, index_x, index_y):
        self.type = type
        self.x = abs(NUMBER_ROW-index_y)-1
        self.y = index_x
        if(type == "x"):
            self.img = arcade.Sprite(path_img_x, IMAGE_SCALING)
        else:
            self.img = arcade.Sprite(path_img_o, IMAGE_SCALING)

        self.img.center_x = calculate_center_position_from_index(index_x)
        self.img.center_y = calculate_center_position_from_index(index_y)
