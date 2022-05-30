from os import system, name

# function to clear the command line
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# ANSI colors
Black   = '\u001b[30m'
Red     = '\u001b[31m'
Green   = '\u001b[32m'
Yellow  = '\u001b[33m'
Blue    = '\u001b[34m'
Magenta = '\u001b[35m'
Cyan    = '\u001b[36m'
White   = '\u001b[37m'
Reset   = '\u001b[0m'
    
# ANSI bold
Bold = '\u001b[1m'

def intro():
    # red colour
    print(f"{Red}{Bold}")
    print("|--||--|                |--||--|                  |--||--|               ") 
    print("   ||    --|--  |----      ||     |----|  |----      ||     |----|  |----")
    print("   ||      |    |          ||     |....|  |          ||     |    |  |~~~~")
    print("   ||    __|__  |____      ||     |    |  |____      ||     |____|  |____")
    print(f"{Reset}\n\n")
 
    # yellow colour
    print(f"{Yellow}")
    print('|--- Instructions to Play ---|\n')
    print('Enter the number on the block to place ur choice over there.')
    print('Inputs should be in the range (1-9).\n')
    board = [1, 2, 3, 4, 5, 6 ,7, 6, 9]
    
    # green colour
    print(f"{Green}")
    draw_board(board)
    input(f'\n{Magenta}Press {Reset}{Bold}Enter{Reset}{Magenta} to start the game..')
    print(f"{Reset}")


# user input  
# - countinues to take input unless user gives
#   free block from 1-9
def user_input(board):

    user_in = "No_Input"
    accepted_range = range(1,10)
    within_range = False

    while not user_in.isdigit() or not within_range:
        
        user_in = input(" (1-9): ")

        if user_in.isdigit():
            if int(user_in) in accepted_range:
                if board[int(user_in)-1] == ' ':
                    within_range = True
                else:
                    print(f"{Red}Block is full{Reset}")
    
    return int(user_in)
 
# draws the board from given values
def draw_board(row):
    # green colour
    print("\u001b[32m")
    for i in range(0,7,3):
        print("  ", row[i], " ", "|", " ", row[i+1], " ", "|", " ", row[i+2], " ")
        if i < 6:
            print(" - - -", "|", "- - -", "|", "- - -")
    print("\u001b[0m")
 

# checks for win 
# - The possible combinations to win are 
#   only -rows -coloumns -diagonals 

def check_win(board):
    winning_seqs = [
        # rows
        [1,2,3],[4,5,6],[7,8,9],
        # columns
        [1,4,7],[2,5,8],[3,6,9],
        # diagonals
        [1,5,9],[3,5,7]           
    ]
    
    win = True
    for seq in winning_seqs:
        win = True
        ch = board[seq[0]-1]
        for i in seq:
            if board[i-1] != ch or board[i-1] == ' ':
                win = False
                break

        if win:
            for i in seq:
                board[i-1]= Red + board[i-1] + Green
            clear()
            print(f'{Bold}{Yellow} <|> {Red}Congratulations {Yellow}<|> {Reset}')
            draw_board(board)
            print(f'{Red}    {board[seq[0]-1]}{Green} wins the Game{Reset}\n')
            return win

    return win

intro()
clear()

# Resetting board to ' ' values from numbers

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print(f"{Red}({Yellow}-=<{Red}| {Cyan}{Bold}Tic Tac Toe {Red}|{Yellow}>=-{Red}){Reset}\n")
draw_board(board)


def Play():
    # i to keep track of whose turn 
    i = 0

    # while loop runs until someonewins
    while(not check_win(board)): 

        # no wins if it is a draw 
        # hence check if board is full
        if ' ' not in board:
            print(f"{Red}   X{Green} and {Red}O{Green} its a Tie{Reset}")
            break
    
        if i%2 == 0:
            print(f"\n:: X's turn ::", end="")
            x_in = user_input(board)
            board[x_in - 1] = 'X'
        else:
            print(f"\n:: O's turn ::", end="")
            o_in = user_input(board)
            board[o_in - 1] = 'O'
    

        i = i + 1
        clear()
        print(f"{Red}({Yellow}-=<{Red}| {Cyan}{Bold}Tic Tac Toe {Red}|{Yellow}>=-{Red}){Reset}\n")
        draw_board(board)

Play()
