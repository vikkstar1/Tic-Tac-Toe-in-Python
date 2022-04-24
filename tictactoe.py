#tic tac toe game
from array import *

#The players
player_one = 'X'
player_two = 'O'
#Player index variable
#The board
board = ['1','2','3','4','5','6','7','8','9' ]             #board initialisation
    #board positions

#The initial draw of the board 
def draw():
    print("  |  |  ")
    print("_"+str(board[0])+"|_"+str(board[1])+"|_"+str(board[2]))
    print("  |  |  ")
    print("_"+board[3]+"|_"+board[4]+"|_"+board[5])
    print("  |  |  ")
    print(" "+board[6]+"| "+board[7]+"| "+board[8])

def whatplayer(last_player):
    if(last_player == player_one):
        last_player = player_two
        return last_player
    elif(last_player == player_two):
        last_player = player_one
        return last_player

#check if cell is empty
def is_free(x):
    if x != 'X' and x!='O':
        return True
    else:
        return False

def move(player):
    position = int(input('Enter the position you want to place your player: '))
    #player = whatplayer(last_player)
    if(int(position) <=9 and int(position) >= 1):                            
            if(is_free(board[position-1])):         #check if the cell empty
                 board[position-1] = player       #setting the cells value to the players value
            else:
                 print("You cannot move here")
    else:
            print("Not a valid cell")
            move(player)

def vertical_win():
    if(board[0] == board[3] and board[3] == board[6]):
        return True 
    elif(board[1] == board[4] and board[4] == board[7]):
        return True
    elif(board[2] == board[5] and board[5] == board[8]):
        return True
    else:
        return False

def horizontal_win():
    if(board[0] == board[1] and board[1] == board[2]):
        return True 
    elif(board[3] == board[4] and board[4] == board[5]):
        return True
    elif(board[6] == board[7] and board[7] == board[8]):
        return True
    else:
        return False

def diagonal_win():
    if(board[0] == board[4] and board[4] == board[8]):
        return True
    elif(board[2] == board[4] and board[4] == board[6]):
        return True
    else:
        return False    

def game_over():
    if(vertical_win() or horizontal_win() or diagonal_win()):
        return True
    else:
        return False

#game logic -- main function
def run_game():
    last_player = player_one
    while True:
        draw()
        last_player = whatplayer(last_player)
        move(whatplayer(last_player))
        if(game_over()):
            draw()
            break
    print("The Game is Over. You won")

run_game()