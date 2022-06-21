import random
import math
                                                        #MinMax Algorithm
def is_free(x):
    if x != 'X' and x!='O':
        return True
    else:
        return False


def count_free_cells(board):
    count = 0
    for i in range(9):
        if is_free(board[i]):
            count = count +1

    print(count)        
    return count

def min_max(player,board):
    high_score = -math.inf
    available_moves = count_free_cells(board)
    for move in available_moves:
        board[move-1] = player
        #score = 