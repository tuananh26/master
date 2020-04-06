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
    if(x in range(0, NUMBER_COLUMN) and y in range(0, NUMBER_ROW)):
        return False
    return True


def is_victory(index_x, index_y, type_chess, board):
    # detect nearly chess
    count = 1
    # check horizontal
    for row in board:
        print(row)

    print("right")
    while(True):
        if(count >= 5):
            break
        index_x += 1
        if(out_of_index(index_x, index_y)):
            break
        if(board[index_x][index_y] != type_chess):
            break
        # print("x=", index_x)
        # print("y= ", index_y)
        # print(board[index_x][index_y])
        count += 1

    print("left")
    while(True):
        if(count >= 5):
            break
        index_x -= 1
        if(out_of_index(index_x, index_y)):
            break
        if(board[index_x][index_y] != type_chess):
            break
        # print("x=", index_x)
        # print("y= ", index_y)
        # print(board[index_x][index_y])
        count += 1

    print(count)
    if(count == 5):
        print("win")
        return True

    return False
