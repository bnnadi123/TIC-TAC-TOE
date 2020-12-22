

def display_board(board):
    print(board[6]+'|'+board[7]+'|'+board[8])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[2]+'|'+board[1]+'|'+board[0])



def player_input():
    Player1 = input('Player 1 choose between X or O: ')
    while Player1 not in ['X','O']:
        print('Invalid input, re-enter marker')
        Player1 = input('Player 1 choose between X or O: ')
    if Player1=='X':
        Player2='O'
    else:
        Player2='X'
    name1 = input("Enter your player name: ")
    name2 = input("Enter your player name: ")
    print(f'{name1} is for {Player1}')
    print(f'{name2} is for {Player2}')
    return(Player1,Player2)
        
    
def place_marker(board,marker,position):
    board[position]= marker


def win_checker(board,marker):
    if board[8]==board[7]==board[6]==marker:
        win =True
    elif board[3]== board[4]==board[5]==marker:
         win =True
    elif board[0]==board[1]==board[2]==marker:
         win =True
    elif board[2]==board[3]==board[6]==marker:
         win =True
    elif board[1]==board[4]==board[7]==marker:
         win =True
    elif board[0]==board[5]==board[8]==marker:
         win =True
    elif board[2]==board[4]==board[8]==marker:
         win =True
    elif board[0]==board[4]==board[6]==marker:
         win =True
    else:
        win = False
    return win
  

import random

def choose_first():
    player = random.randint(1,2)
    if player == 1:
        return "Player 1"
    else:
        return "Player 2"
    
  

def space_check(board,position):
    if board[position]=="":
        return True
    else:
        return False


def full_board_check(board):
    for i in range(0,9):
        if board[i] == "":
            return False
  
    return True


def player_choice(board):
    within_range = False
    space = False
    while  within_range==False or space==False:
        choice = int(input('Enter the position you want to play(0-8): '))
        if choice  in range(0,9):
            within_range=True
        else:
            within_range=False
            print('Digit entered not in range of values')
            
        if within_range==True:
            if space_check(board,choice):
                space = True
            else:
                space =False
                print('This space is occupied')
    return choice
               
    
def replay():
    ans = 'Wrong'
    while ans not in ['Y','N']:
        ans = input('Do you want to play again(Y or N): ').capitalize()
    return ans == 'Y'

  

board =['','','','','','','','','']

#welcome to the tic tac toe game
print('WELCOME TO TIC TAC TOE!')
while True:
    #displays the board game
    display_board(board)
    # Players choose your marker
    x,y=player_input()
    print(x,y)
    
    player=choose_first()
    print(f'player with marker {player} goes first')
    play_game = input("Do you play(Y or N): ").capitalize()
    if play_game == 'Y':
      game_on = True
    elif play_game == 'N':
      game_on = False
  
    while game_on:
      if player =='Player 1':
            Player1 = player_choice(board)
            place_marker(board,x,Player1)
            display_board(board)
          
            if win_checker(board,x):
              display_board(board)
              print('Player 1 wins the game')
              game_on = False

            else:
              #player 1 has not won yet
              if full_board_check(board):
                display_board(board)
                print("This is a tie")
                game_on = False
              else:
                #player 1 has not one and it is not a full board
                player = 'Player 2'
      else:
            Player2 = player_choice(board)
            place_marker(board,y,Player2)
            display_board(board)
          
            if win_checker(board,y):
              display_board(board)
              print('Player 2 wins the game')
              game_on = False

            else:
              #player 2 has not won yet
              if full_board_check(board):
                display_board(board)
                print("This is a tie")
                game_on = False
              else:
                #player 1 has not one and it is not a full board
                player = 'Player 1'
    if not replay():
      break
    




            
        
           