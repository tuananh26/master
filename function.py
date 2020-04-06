from definiteClass import Index
from chess import Chess
from const import NUMBER_COLUMN, NUMBER_ROW


def is_chess_exists(chess, list_chess):
    for item in list_chess:
        if(item.x == chess.x and item.y == chess.y):
            return True
    return False


def switch_type(type):
    if(type == "x"):
        return "o"
    else:
        return "x"


def out_of_index(x, y):
    if(x in range(0, NUMBER_ROW) and y in range(0, NUMBER_COLUMN)):
        return False
    print("out of index")
    return True


def is_victory(index_x, index_y, type_chess, board):
    # detect nearly chess

    # check horizontal

    for row in board:
        print(row)
    print("check horizontal")
    count = 1
    x = index_x
    y = index_y
    while(count < 5):
        y += 1
        if(out_of_index(x, y)or board[x][y] != type_chess):
            break
        count += 1

    x = index_x
    y = index_y
    while(count < 5):
        y -= 1
        if(out_of_index(x, y)or board[x][y] != type_chess):
            break
        count += 1

    print("count = ", count)
    if(count == 5):
        return True

    # check vertical
    print("check vertical")
    count = 1
    x = index_x
    y = index_y
    while(count < 5):
        x += 1
        if(out_of_index(x, y)or board[x][y] != type_chess):
            break
        count += 1

    x = index_x
    y = index_y
    while(count < 5):
        x -= 1
        if(out_of_index(x, y)or board[x][y] != type_chess):
            break
        count += 1

    print("count = ", count)
    if(count == 5):
        return True

    # check dianol
    print("check dianol \\")
    count = 1
    x = index_x
    y = index_y
    while(count < 5):
        x += 1
        y += 1
        if(out_of_index(x, y)or board[x][y] != type_chess):
            break
        count += 1

    x = index_x
    y = index_y
    while(count < 5):
        x -= 1
        y -= 1
        if(out_of_index(x, y)or board[x][y] != type_chess):
            break
        count += 1

    print("count = ", count)
    if(count == 5):
        return True

    print("check dianol //")
    count = 1
    x = index_x
    y = index_y
    while(count < 5):
        x -= 1
        y += 1
        if(out_of_index(x, y)or board[x][y] != type_chess):
            break
        count += 1

    x = index_x
    y = index_y
    while(count < 5):
        x += 1
        y -= 1
        if(out_of_index(x, y)or board[x][y] != type_chess):
            break
        count += 1

    print("count = ", count)
    if(count == 5):
        return True
    return False
