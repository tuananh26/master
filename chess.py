
from image import img_x, img_o
from calculate import calculate_index


class Chess:
    def __init__(self, type, width, height):
        if(type == "x"):
            self.img = img_x
        else:
            self.img = img_o

        self.row_index = calculate_index(height)
        self.column_index = calculate_index(width)
