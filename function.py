from definiteClass import Index
from chess import Chess
from const import NUMBER_COLUMN, NUMBER_ROW


def is_chess_exists(chess, list_chess):
    for item in list_chess:
        if(item.index_x == chess.index_x and item.index_y == chess.index_y):
            return True
    return False


def switch_type(type):
    if(type == "x"):
        return "o"
    else:
        return "x"


def is_victory(chess, board):
    # detect nearly chess
    count = 0
    chess_current = chess
    board[chess_current.index_x][chess_current.index_y] = "checked"

    while(True):
        # check horizontal
            # right
        chess_current.index_x += 1
        # out of index column
        if(chess_current.index_x == NUMBER_COLUMN):
            break
        # checked chess
        if(board[chess_current.index_x][chess_current.index_y] == "checked"):
            break
        # different type
        if(board[chess_current.index_x][chess_current.index_y]):
            break

        chess_current.type = board[chess_current.index_x][chess_current.index_y]
        if(count == 5):
            break

    return False
