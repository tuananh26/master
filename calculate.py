from const import PIXEL_WIDTH


def caculate_index(weight):
    return int(weight/PIXEL_WIDTH)


def calculate_position(weight):
    return caculate_index(weight)*PIXEL_WIDTH


def calculate_center_position(weight):
    return calculate_position(weight)+PIXEL_WIDTH/2


def calculate_center_position_from_index(index):
    return index*PIXEL_WIDTH+PIXEL_WIDTH/2


def abs(x):
    if(x > 0):
        return x
    return x*(-1)
