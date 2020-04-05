from definiteClass import Index
from chess import Chess


def is_chess_exists(chess, list_chess):
    for item in list_chess:
        if(item.index_x == chess.index_x and item.index_y == chess.index_y):
            return True
    return False


def is_victory(chess_type, chess_index, board):
    # detect nearly chess
    count = 0
    flag = True
    chess_current = Chess(chess_type, chess_index)
    board[chess_index.x][chess_index.y] = "checked"

    while(True):
        if(count == 5):
            break
        if(flag == False):
            break
        if(chess_current.chess_type != chess_type):
            break
        if(board[chess_current.x][chess_current.y] == "checked"):
            break
        # check horizontal

    return False
