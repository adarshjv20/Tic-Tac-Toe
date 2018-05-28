

def display_board(board):
    print(' {} | {} | {}\n {} | {} | {}\n {} | {} | {}\n'.format(board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9]) )
    print('Follow the input of your Mobile Keypad')

    
    
initial_board = ['#','_','_','_','_','_','_','_','_','_']
play_board = []

##Chooses the first player to play
import random
def choose_first():
    global first
    first = random.randint(1,2)
    if first == 1:
        print ('player 1 goes first')
    elif first ==2:
        print('player 2 goes first')


##Assign marker to a player
def player_input():
    global player1,player2
    marker = True
    while marker:
        if first==1:
            player1 = input('Player1 which marker would you like an "X" or an "O"--->')
            if player1.lower() == 'x' or player1.lower() == 'o':
                break
        elif first==2:
            player2 = input('Player2 which marker would you like an "X" or an "O"--->')
            if player2.lower() == 'x' or player2.lower() == 'o':
                break
    if first ==1:
        if player1.lower() == 'x':
            player2 = 'o'
            print('Player2 gets "o"')
        else:
            player2 = 'x'
            print('Player2 gets "X"')
    if first== 2:
        if player2.lower() == 'x':
            player1 = 'o'
            print('Player1 gets "o"')
        else:
            player1 = 'x'
            print('Player1 gets "X"')


##Players take turns
def change_player():
    global position,first
    if first == 1 :
        while True:
            position = int(input('Player 1 mark the next available space'))
            if (position in range(1,10)) and (space_check(play_board,position)):
                break        
        first = 2
    elif first == 2:
        while True:
            position = int(input('Player 2 mark the next available space'))
            if (position in range(1,10)) and (space_check(play_board,position)):
                break
        first = 1
		
		
##Places the marker on the board
def place_marker(board, marker, pos):
    global play_board
    play_board[pos]=marker.upper()



## To check if a player has won
def win_check(board, mark):
    if (board[1]==mark and board[2]==mark and board[3]==mark) or (board[4]==mark and board[5]==mark and board[6]==mark) or (board[7]==mark and board[8]==mark and board[9]==mark):
        return True
    elif ((board[1]==mark and board[4]==mark and board[7]==mark)) or (board[2]==mark and board[5]==mark and board[8]==mark) or(board[3]==mark and board[6]==mark and board[9]==mark):
        return True
    elif ((board[3]==mark and board[5]==mark and board[7]==mark)) or (board[1]==mark and board[5]==mark and board[9]==mark):
        return True
    else:
        return False


## Check if the marker can be placed in the given position
def space_check(board, position):
    #print(board[position].lower())
    if board[position].lower()=='x' or board[position].lower()== 'o':
        return False
    else:
        return True


## check if the board is filled
def full_board_check(board):
    for i in range(1,10):
        #print(board[i].lower())
        if (board[i].lower() != 'x' and  board[i].lower()!='o'):
            return False
    return True


##TCheck if the players want to play another game
def replay():
    while True:
        again = input('Do you want to play again "yes or "no"')
        if again.lower() == 'yes' or again.lower() == 'y':
            return True
        elif again.lower() == 'no' or again.lower() == 'n':
            print('BYEEEE')
            return False


## RUN THE GAME
print('Welcome to Tic Tac Toe!')
while True:
    # print('\n'*100)
    choose_first()
    player_input()
    display_board(initial_board)
    play_board = list(initial_board)
    while True:
        change_player()
        if first == 2:
            print('\n'*40)
            place_marker(play_board,player1,position)
            display_board(play_board)
            if win_check(play_board,player1.upper()):
                print('Player 1 WON!!!!!')
                break
            elif full_board_check(play_board):
                print('ITS A TIE!!!')
                break
        elif first == 1:
            print('\n'*40)
            place_marker(play_board,player2,position)
            display_board(play_board)
            if win_check(play_board,player2.upper()):
                print('Player 2 WON!!!!!')                         
                break
            elif full_board_check(play_board):
                print('ITS A TIE!!!')
                break

    if not replay():
        break
