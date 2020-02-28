import os
os.system('clear')
current_player = ''
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
# board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def choose_player():
  os.system('clear')
  choice = input('Player one please choose X or O\n').upper()
  if choice == "X":
    current_player = choice
  elif choice == "O":
    current_player = choice
  else:
    choose_player()
  return current_player

def check_winner(current_player):
  #horizontal
  if board[1] == current_player and board[2] == current_player and board[3] == current_player:
    win(current_player)
  elif board[4] == current_player and board[5] == current_player and board[6] == current_player:
    win(current_player)
  elif board[7] == current_player and board[8] == current_player and board[9] == current_player:
    win(current_player) 
  
  #vertical
  elif board[1] == current_player and board[4] == current_player and board[7] == current_player:
    win(current_player)
  elif board[2] == current_player and board[5] == current_player and board[6] == current_player:
    win(current_player)
  elif board[3] == current_player and board[6] == current_player and board[9] == current_player:
    win(current_player)

  #diagonal
  elif board[1] == current_player and  board[5] == current_player and  board[9] == current_player:
    win(current_player)
  elif board[3] == current_player and board[5] == current_player and  board[7] == current_player:
    win(current_player)
  else:
    pass

def win(current_player):
  os.system('clear')
  print_board()
  print('{} wins!'.format(current_player))
  again = input('Would you like to play again?').upper()
  if again == 'N':
    exit()
  elif again == 'Y':
    turn(choose_player())


def print_board():
  print('| {} | {} | {} |'.format(board[1], board[2], board[3]))
  print('| {} | {} | {} |'.format(board[4], board[5], board[6]))
  print('| {} | {} | {} |'.format(board[7], board[8], board[9]))


def turn(current_player):
  os.system('clear')
  print_board()
  move  = int(input('Player {}, make yo move!\n'.format(current_player)))

  if board[move] == ' ':
    board[move] = current_player
  else:
    print('Spot already taken!')
    turn(current_player)
  board[move] = current_player
  check_winner(current_player)

  if current_player == 'X':
    current_player = 'O'
    turn(current_player)
  else:
    current_player = 'X'
    turn(current_player)


turn(choose_player())