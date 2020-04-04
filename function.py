def is_chess_exists(list, x, y):
    for item in list:
        if(item == [x, y]):
            return True

    return False
